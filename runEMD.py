from EvolutionaryModelDiscovery import *
import numpy as np

def cindexObjective(results):
    #print(np.mean(results.iloc[-1]))
    return np.mean(results.iloc[-1])

modelPath = "ABM_bitcoin.nlogo"
setup = ['setup',
         'set miners-init 146 + random 3 - random 3',
         'set max-init-hashrate  0.0000023 + random-float 0.0000001 - random-float 0.0000001',
         'set min-energy-cost 0.0600000',
         'set hashrate-growth-rate 0.12 + random-float 0.005 - random-float 0.05',
         'set miner-increment-rate 7',
         'set max-energy-cost 0.45',
         'set min-energy-efficiency 0.0001',
         'set max-energy-efficiency 44 + random-float 2 - random-float 2',
         'set loss-tolerance 0.35 + random-float 0.02 - random-float 0.02',
         'set equipment-growth-stop 140 + random 5 - random 5'
         ]
measurements = ["error-term"]
netlogoPath = '/home/dezarg/Downloads/UCF_PhD_semester2/NetLogo-6.1.1-64/NetLogo 6.1.1'
ticks = 1186
emd = EvolutionaryModelDiscovery(netlogoPath = netlogoPath, modelPath=modelPath, setupCommands=setup,
                                 measurementCommands=measurements, ticksToRun=ticks)
emd.setObjectiveFunction(cindexObjective)
emd.setMutationRate(0.2)
emd.setCrossoverRate(0.7)
emd.setGenerations(50)
emd.setReplications(1)
emd.setDepth(2, 5)
emd.setPopulationSize(200)
emd.setIsMinimize(True)


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    emd.evolve()