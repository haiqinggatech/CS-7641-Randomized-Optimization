import matplotlib.pyplot as plt
import pandas

def plot_learning_curve(iterations, train_scores, test_scores, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    plt.ylim((.2, 0.9))
    
    # if datasetNum == 1:
    #     plt.ylim((.55, 1.01))

    plt.xlabel("# Iterations")
    plt.ylabel("ACC Score")
    
    plt.grid()
    
    plt.plot(iterations, train_scores,  color="r",
             label="Training score")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(iterations, test_scores,  color="g",
             label="Test Score")

    plt.legend(loc="best")
    return plt


def plot_mse(iterations, train_scores, test_scores, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    plt.ylim((0.06,0.2))
    
    # if datasetNum == 1:
    #     plt.ylim((.55, 1.01))

    plt.xlabel("# Iterations")
    plt.ylabel("MSE")
    
    plt.grid()
    
    plt.plot(iterations, train_scores,'o-',  color="r",
             label="Training score")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(iterations, test_scores, 'o-', color="g",
             label="Test Score")

    plt.legend(loc="best")
    return plt





def plot_timing_curve(iterations, timeDuration, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    # plt.ylim((.3, 1.01))
    
    # if datasetNum == 1:
    #     plt.ylim((.55, 1.01))

    plt.xlabel("# Iterations")
    plt.ylabel("Training Time (s)")
    
    plt.grid()
    
    plt.plot(iterations, timeDuration, 'o-', color="r",
             label="Duration")

    plt.legend(loc="best")
    return plt



df = pandas.read_csv('BACKPROP_LOG.csv')
title  = 'BACKPROP Result with \n inputlayer = 1, hiddenlayer1= 16, hiddenlayer2= 9, hiddenlayer1= 6'
plot = plot_learning_curve(df['iteration'], df['acc_tst'], df['acc_trg'], title)
plot.savefig('plots/' + title+ '.png')
plot.close()

plot = plot_timing_curve(df['iteration'], df['elapsed'], title + ' Training Time')
plot.savefig('plots/' + title.replace(' ', '_').replace('.', 'pt').lower() + '_time.png')
plot.close()   

plot = plot_mse(df['iteration'], df['MSE_tst'], df['MSE_trg'], title)
plot.savefig('plots/' + title+ 'MSE''.png')
plot.close()

