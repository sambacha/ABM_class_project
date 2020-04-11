from EvolutionaryModelDiscovery import *
import numpy as np

def cindexObjective(results):
    #print(np.mean(results.iloc[-1]))
    return (-1) * np.mean(results.iloc[-1])

modelPath = "ABM_bitcoin.nlogo"
setup = ['setup']
measurements = ["error-term"]
netlogoPath = '/home/dezarg/Downloads/UCF_PhD_semester2/NetLogo-6.1.1-64/NetLogo 6.1.1'
ticks = 1186
emd = EvolutionaryModelDiscovery(netlogoPath = netlogoPath, modelPath=modelPath, setupCommands=setup,
                                 measurementCommands=measurements, ticksToRun=ticks)
emd.setObjectiveFunction(cindexObjective)
emd.setMutationRate(0.1)
emd.setCrossoverRate(0.7)
emd.setGenerations(10)
emd.setReplications(3)
emd.setDepth(2, 7)
emd.setPopulationSize(20)


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    emd.evolve()