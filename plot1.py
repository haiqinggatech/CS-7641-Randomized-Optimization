import matplotlib.pyplot as plt
import pandas




# sa1 = pandas.read_csv('CONTPEAKS_SA0.15_1_LOG.csv')
# sa2 = pandas.read_csv('CONTPEAKS_SA0.35_1_LOG.csv')
# sa3 = pandas.read_csv('CONTPEAKS_SA0.55_1_LOG.csv')
# sa4 = pandas.read_csv('CONTPEAKS_SA0.75_1_LOG.csv')
# sa5 = pandas.read_csv('CONTPEAKS_SA0.95_1_LOG.csv')


# GA = pandas.read_csv('KS_GA100_30_30_1_LOG.csv')
# MIMIC = pandas.read_csv('KS_MIMIC100_50_0.7_1_LOG.csv')
# SA = pandas.read_csv('KS_SA0.55_1_LOG.csv')
# RHC = pandas.read_csv('KS_RHC_1_LOG.csv')
# title  = 'Knapsack Problem Fitness Comparision'
# plt.figure()
# plt.title(title)

    

# plt.xlabel("# Iterations")
# plt.ylabel("Fitness Function")
# # plt.ylabel("Running Time")
# plt.ylim((1750, 3600))
# plt.xlim((0, 5000))
    
# plt.grid()

# plt.plot(GA['iterations'], GA['fitness'], color="r",label='Genetic Algorithms')
# plt.plot(SA['iterations'], SA['fitness'], color="b",label="Simulated Annealing")
# plt.plot(RHC['iterations'], RHC['fitness'], color="y",label="Randomized Hill Climbing")
# plt.plot(MIMIC['iterations'], MIMIC['fitness'], color="c",label="MIMIC")

# plt.legend(loc="best")





# plt.savefig('plots/' + title+ '.png')
# plt.close()

# plt.figure()
# title  = 'Knapsack Problem Running Time Comparision'
# plt.title(title)

# plt.xlabel("# Iterations")
# plt.ylabel("Running Time")
# # plt.ylabel("Running Time")
# plt.ylim((0, 7))
# plt.xlim((0, 5000))
    
# plt.grid()
    
# plt.plot(GA['iterations'], GA['time'], color="r",label='Genetic Algorithms')
# plt.plot(SA['iterations'], SA['time'], color="b",label="Simulated Annealing")
# plt.plot(RHC['iterations'], RHC['time'], color="y",label="Randomized Hill Climbing")
# plt.plot(MIMIC['iterations'], MIMIC['time'], color="c",label="MIMIC")

# plt.legend(loc="best")

# sa1 = pandas.read_csv('KS_MIMIC100_50_0.1_1_LOG.csv')
# sa2 = pandas.read_csv('KS_MIMIC100_50_0.3_1_LOG.csv')
# sa3 = pandas.read_csv('KS_MIMIC100_50_0.5_1_LOG.csv')
# sa4 = pandas.read_csv('KS_MIMIC100_50_0.7_1_LOG.csv')
# sa5 = pandas.read_csv('KS_MIMIC100_50_0.9_1_LOG.csv')



# plt.savefig('plots/' + title+ '.png')
# plt.close()

# plt.figure()



sa1 = pandas.read_csv('CONTPEAKS_GA100_10_10_1_LOG.csv')
sa2 = pandas.read_csv('CONTPEAKS_GA100_10_30_1_LOG.csv')
sa3 = pandas.read_csv('CONTPEAKS_GA100_30_10_1_LOG.csv')
sa4 = pandas.read_csv('CONTPEAKS_GA100_30_30_1_LOG.csv')
sa5 = pandas.read_csv('CONTPEAKS_GA100_50_10_1_LOG.csv')
sa6 = pandas.read_csv('CONTPEAKS_GA100_50_30_1_LOG.csv')
plt.xlabel("# Iterations")
plt.ylabel("Running Time ")
# plt.ylabel("Running Time")
plt.xlim((0, 5000))
plt.ylim((0, 0.5))
plt.grid()


plt.plot(sa1['iterations'], sa1['time'], color="r",label="mutation 10 mate 10")
plt.plot(sa2['iterations'], sa2['time'], color="b",label="mutation 10 mate 30")
plt.plot(sa3['iterations'], sa3['time'], color="y",label="mutation 30 mate 10")
plt.plot(sa4['iterations'], sa4['time'], color="c",label="mutation 30 mate 30")
plt.plot(sa5['iterations'], sa5['time'], color="m",label="mutation 50 mate 10")
plt.plot(sa5['iterations'], sa6['time'], color="k",label="mutation 50 mate 30")

title  = 'Continuous Peaks Iterations Vs Running Time -GA'
plt.xlim((0, 5000))
# plt.xlabel("# Iterations")
# plt.ylabel("Fitness ")
# plt.grid()
plt.legend(loc="best")
plt.title(title)
plt.savefig('plots/' + title+ '.png')
plt.close()


# #MIMIC





# # plt.xlabel("# Iterations")
# # # plt.ylabel("Fitness ")
# # plt.ylabel("Running Time")
# # plt.xlim((1500, 3500))
# # # plt.ylim((0, 0.12))

# # plt.plot(sa1['iterations'], sa1['fitness'], color="r",label="mutation 10 mate 10")
# # plt.plot(sa2['iterations'], sa2['fitness'], color="b",label="mutation 10 mate 30")
# # plt.plot(sa3['iterations'], sa3['fitness'], color="y",label="mutation 30 mate 10")
# # plt.plot(sa4['iterations'], sa4['fitness'], color="c",label="mutation 30 mate 30")
# # plt.plot(sa5['iterations'], sa5['fitness'], color="m",label="mutation 50 mate 10")
# # plt.plot(sa5['iterations'], sa6['fitness'], color="k",label="mutation 50 mate 30")

# # plt.grid()
# # title  = 'Knapsack Problem Iterations Vs Fitness -GA'
# # plt.legend(loc="best")
# # plt.title(title)
# # plt.savefig('plots/' + title+ '.png')
# # plt.close()


# plt.figure()
# plt.xlabel("# Iterations")
# plt.ylabel("Time ")
# # plt.ylabel("Running Time")
# plt.xlim((0, 5000))
# plt.ylim((0, 8))


    
# plt.grid()

# plt.plot(sa1['iterations'], sa1['time'], color="r",label="0.1")
# plt.plot(sa2['iterations'], sa2['time'], color="b",label="0.3")
# plt.plot(sa3['iterations'], sa3['time'], color="y",label="0.5")
# plt.plot(sa4['iterations'], sa4['time'], color="c",label="0.7")
# plt.plot(sa5['iterations'], sa5['time'], color="m",label="0.9")
# # plt.plot(sa6['iterations'], sa6['time'], color="K",label="mutation 50 mate 30")
# title  = 'Knapsack Problem Iterations Vs Running Time -MIMIC'




# plt.legend(loc="best")

# plt.title(title)



# plt.savefig('plots/' + title+ '.png')
# plt.close()

# # # plt.xlabel("# Iterations")
# # plt.ylabel("Running Time")
# # # plt.ylabel("Running Time")
# # plt.xlim((0, 5000))
# # plt.ylim((0, 300))


    
# # plt.grid()

# # plt.plot(sa1['iterations'], sa1['time'], color="r",label='0.15')
# # plt.plot(sa2['iterations'], sa2['time'], color="b",label="0.35")
# # plt.plot(sa3['iterations'], sa3['time'], color="y",label="0.55")
# # plt.plot(sa4['iterations'], sa4['time'], color="c",label="0.75")
# # plt.plot(sa5['iterations'], sa5['time'], color="m",label="0.95")
# # title  = 'Continuous Peaks Iterations Vs Running Time -SA'


# # plt.legend(loc="best")

# # plt.title(title)



# # plt.savefig('plots/' + title+ '.png')
# # plt.close()

