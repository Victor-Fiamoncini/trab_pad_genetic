from __future__ import print_function
import numpy as np

ex_array = np.zeros((100000), dtype='uint8')

for index in range(0, 100000):
  ex_array[index] = 1
  print('Yay! {} done!'.format(index))
