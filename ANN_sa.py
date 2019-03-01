"""
Backprop NN training on titanic data
"""
import os
import csv
import time
import sys
sys.path.append('/Volumes/Work/Gatech/cs7641/Previous report/CS7641-master/HW2/ABAGAIL/ABAGAIL.jar')
from func.nn.backprop import BackPropagationNetworkFactory
from shared import SumOfSquaresError, DataSet, Instance
from opt.example import NeuralNetworkOptimizationProblem
from func.nn.backprop import RPROPUpdateRule, BatchBackPropagationTrainer
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
from func.nn.activation import LogisticSigmoid

# Network parameters found "optimal" in Assignment 1
INPUT_LAYER = 26
HIDDEN_LAYER1 =16

HIDDEN_LAYER2 =9
HIDDEN_LAYER3 =6


OUTPUT_LAYER = 1
TRAINING_ITERATIONS = 20000
OUTFILE = './XXX_LOG.csv'


def initialize_instances(infile):
    """Read the m_trg.csv CSV data into a list of instances."""
    instances = []

    # Read in the CSV file
    with open(infile, "r") as dat:
        reader = csv.reader(dat)

        for row in reader:
            instance = Instance([float(value) for value in row[:-1]])
            instance.setLabel(Instance(0 if float(row[-1]) <= 0 else 1))
            instances.append(instance)

    return instances
	

def errorOnDataSet(network,ds,measure):
    N = len(ds)
    error = 0.
    correct = 0
    incorrect = 0
    for instance in ds:
        network.setInputValues(instance.getData())
        network.run()
        actual = instance.getLabel().getContinuous()
        predicted = network.getOutputValues().get(0)
        predicted = max(min(predicted,1),0)
        if abs(predicted - actual) < 0.5:
            correct += 1
        else:
            incorrect += 1
        output = instance.getLabel()
        output_values = network.getOutputValues()
        example = Instance(output_values, Instance(output_values.get(0)))
        error += measure.value(output, example)
    MSE = error/float(N)
    acc = correct/float(correct+incorrect)
    return MSE,acc
	
	
def train(oa, network, oaName, training_ints, testing_ints, measure):
    """Train a given network on a set of instances.
    """
    print "\nError results for %s\n---------------------------" % (oaName,)
    times = [0]
    for iteration in xrange(TRAINING_ITERATIONS):
        start = time.clock()
        oa.train()
        elapsed = time.clock()-start
    	times.append(times[-1]+elapsed)
        if iteration % 10 == 0:
    	    MSE_trg, acc_trg = errorOnDataSet(network,training_ints,measure)
            MSE_tst, acc_tst = errorOnDataSet(network,testing_ints,measure)
            txt = '{},{},{},{},{},{}\n'.format(iteration,MSE_trg,MSE_tst,acc_trg,acc_tst,times[-1]);print txt
            with open(OUTFILE.replace('XXX',oaName),'a+') as f:
                f.write(txt)

def main(T, CE):
    """Run this experiment"""
    training_ints = initialize_instances('training_data.csv')
    testing_ints = initialize_instances('testing_data.csv')
    factory = BackPropagationNetworkFactory()
    measure = SumOfSquaresError()
    data_set = DataSet(training_ints)
    acti = LogisticSigmoid()
    rule = RPROPUpdateRule()
    oa_name = "SA_{}_{}".format(T, CE)
    with open(OUTFILE.replace('XXX',oa_name),'w') as f:
        f.write('{},{},{},{},{},{}\n'.format('iteration','MSE_trg','MSE_tst','acc_trg','acc_tst','elapsed'))
    classification_network = factory.createClassificationNetwork([INPUT_LAYER, HIDDEN_LAYER1, OUTPUT_LAYER],acti)
    nnop = NeuralNetworkOptimizationProblem(data_set, classification_network, measure)
    oa = SimulatedAnnealing(T, CE, nnop)
    train(oa, classification_network, oa_name, training_ints, testing_ints, measure)



if __name__ == "__main__":
   for CE in [0.15,0.35,0.55,0.7,0.95]:
    for  T in [1e8, 1e10, 1e12]:
        main(T, CE)