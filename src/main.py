from threading import Thread
from multiprocessing import Process
from multiprocessing import Pool
import pandas as pd
from itertools import groupby, product
import time

def allele(e):
  allele = []

  for _, v in groupby(e, key=str.lower):
    allele.append(list(v))

  return allele

def punnett(a, b):
  permutations = []

  for e in product(
    *(
      [''.join(e) for e in product(*e)]
      for e in zip(allele(a), allele(b))
    )
  ):
    permutations.append(''.join(e))

  return permutations

if __name__ == '__main__':
  dataset = pd.read_csv('src/dataset.csv')

  crossover_samples = dataset.sample(2)

  crossover_genotypes = []

  for sample in crossover_samples.itertuples():
      crossover_genotypes.append(
        sample.eyeColor 
        + sample.hairColor
        + sample.skinColor
        + sample.dominantHand
        + sample.earLobule
        + sample.noseFormat
        + sample.hairSwirl
        + sample.widowBeak
        # + sample.dimples
        # + sample.ptc
        # + sample.thumb
        # + sample.earTip
        # + sample.eyebrow
        # + sample.freckles
        # + sample.eyelash
        # + sample.eyeFormat
        # + sample.cerumen
        # + sample.wisdowTeeth
      )

  threads = []

  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))
  threads.append(Thread(target=punnett, args=tuple(crossover_genotypes)))

  start = time.time()

  for x in threads:
    x.start()

  for x in threads:
    x.join()

  end = time.time()

  duration = (end - start)

  print(duration)

  start = time.time()

  for x in range(1, 10):
    punnett(crossover_genotypes[0], crossover_genotypes[1])

  end = time.time()

  duration = (end - start)

  print(duration)

  processes = []

  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))
  processes.append(Process(target=punnett, args=tuple(crossover_genotypes)))

  start = time.time()

  with Pool(10) as p:
    punnett(crossover_genotypes[0], crossover_genotypes[1])
  # for process in processes:
  #   process.fork()

  # for process in processes:
  #   process.join()

  end = time.time()

  duration = (end - start)

  print(duration)