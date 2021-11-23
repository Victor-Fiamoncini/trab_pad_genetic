from threading import Thread
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
      + sample.dimples
      + sample.ptc
      + sample.thumb
      + sample.earTip
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

start = time.time()

for x in threads:
  x.start()

for x in threads:
  x.join()

end = time.time()

duration = (end - start)

print(duration)

start = time.time()

for x in range(1, 3):
  punnett(crossover_genotypes[0], crossover_genotypes[1])

end = time.time()

duration = (end - start)

print(duration)