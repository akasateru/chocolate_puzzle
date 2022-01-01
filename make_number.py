import pandas as pd
import numpy as np
import time
import random

# numbers = []

# def make_number(number):
#   global try_count
#   try_count+=1
#   if len(numbers)>=100:
#     return 0
#   if len(number)==12:
#     numbers.append(list(number))
#     return 0
#   else:
#     for i in range(12):
#       if not i in number:
#         number.append(i)
#         make_number(number)
#         number.pop(-1)

# try_count = 0
# make_number(number=[])
# print(try_count)

# np.savetxt('numbers.csv',np.array(numbers),fmt="%d",delimiter=',')

# =-------------------------------------------------------------


np.savetxt('numbers.csv',np.array(numbers),fmt="%d",delimiter=',')