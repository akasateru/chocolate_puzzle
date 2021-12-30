import pandas as pd
import numpy as np
import time

numbers = []

def make_number(number):
  if len(number)==12:
    sorted_number = sorted(number)
    if sorted_number == [0,1,2,3,4,5,6,7,8,9,10,11]:
      numbers.append(list(number))
    return 0
  else:
    for i in range(12):
      number.append(i)
      make_number(number)
      number.pop(-1)

make_number(number=[])

numbers = np.array(numbers)
np.savetxt('numbers.csv',numbers,fmt="%d",delimiter=',')