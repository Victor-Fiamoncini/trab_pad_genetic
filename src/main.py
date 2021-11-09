import os
import pandas as pd
import numpy as np
from itertools import permutations, groupby, product

data_set_path = os.path.join(os.getcwd(), 'src/dataset.csv')
data_set = pd.read_csv(data_set_path)

del data_set['index']

# data_set = data_set._slice(slice(0, 2))

# crossover_samples = data_set.sample(2)

punnett_square = np.empty([4, 4], dtype=str)


for index, row in data_set.iterrows():
  eye_color_gene = row['eyeColor']
  hair_color_gene = row['hairColor']

  print(eye_color_gene)

  for index, row in data_set.iterrows():
    pass

# print([''.join(p) for p in permutations('OoCc')])


def allele(e):
  return [list(v) for _, v in groupby(e, key = str.lower)]

def punnett(a, b):
  # meteu essa:
  return [''.join(e) for e in product(*([''.join(e) for e in product(*e)] for e in zip(allele(a), allele(b))))]

print(punnett('AaBb', 'AaBb'))
