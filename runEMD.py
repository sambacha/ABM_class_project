from EvolutionaryModelDiscovery import *
import numpy as np

def cindexObjective(results):
    #print(np.mean(results.iloc[-1]))
    return (-1) * np.mean(results.iloc[-1])

modelPath = "ABM_bitcoin.nlogo"
setup = ['setup',
         'set miners-init 146 + random 5 - random 5',
         'set max-init-hashrate  0.0000023 + random-float 0.0000002 - random-float 0.0000002',
         'set min-energy-cost 0.0600000',
         'set hashrate-growth-rate 0.12 + random-float 0.01 - random-float 0.1',
         'set miner-increment-rate 7',
         'set max-energy-cost 0.45',
         'set min-energy-efficiency 0.0001',
         'set max-energy-efficiency 44 + random-float 4 - random-float 4',
         'set loss-tolerance 0.35 + random-float 0.05 - random-float 0.05',
         'set equipment-growth-stop 140 + random 20 - random 20'
         ]
measurements = ["error-term"]
netlogoPath = '/home/dezarg/Downloads/UCF_PhD_semester2/NetLogo-6.1.1-64/NetLogo 6.1.1'
ticks = 1186
emd = EvolutionaryModelDiscovery(netlogoPath = netlogoPath, modelPath=modelPath, setupCommands=setup,
                                 measurementCommands=measurements, ticksToRun=ticks)
emd.setObjectiveFunction(cindexObjective)
emd.setMutationRate(0.1)
emd.setCrossoverRate(0.7)
emd.setGenerations(100)
emd.setReplications(3)
emd.setDepth(4, 10)
emd.setPopulationSize(100)


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    emd.evolve()