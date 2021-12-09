import pymp

ex_array = pymp.shared.array((100000), dtype='uint8')

with pymp.Parallel(4) as p:
  for index in p.range(0, 100000):
    ex_array[index] = 1
    p.print('Yay! {} done!'.format(index))
