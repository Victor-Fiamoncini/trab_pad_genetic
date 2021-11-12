import os
import pandas as pd
from itertools import groupby, product
import _thread
import time

data_set_path = os.path.join(os.getcwd(), 'src/dataset.csv')
data_set = pd.read_csv(data_set_path)

del data_set['index']

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

  print(permutations)

  return permutations

try:
  _thread.start_new_thread(punnett, ('AaBb', 'AaBb'))
  _thread.start_new_thread(punnett, ('AaBb', 'AaBb'))
except:
  print("Error: unable to start thread")

while 1:
  pass
