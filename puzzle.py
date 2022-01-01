import pandas as pd
import numpy as np
import time
import random

random.seed(7)

success = [[1]*6 for i in range(10)]
result = [[0]*6 for i in range(10)]
result_pzl = [[0]*6 for i in range(10)]

puzzle = [[[1,1,1],[1,0,1]],
          [[1,1,0],[0,1,1],[0,0,1]],
          [[1,1,0],[0,1,1],[0,1,0]],
          [[1,1,1],[0,1,0],[0,1,0]],
          [[0,1],[1,1],[1,0],[1,0]],
          [[0,1,0],[1,1,1],[0,1,0]],
          [[0,0,0,1],[1,1,1,1]],
          [[1],[1],[1],[1],[1]],
          [[0,1,1],[0,1,0],[1,1,0]],
          [[1,1,0],[1,1,1]],
          [[1,1,1,1],[0,1,0,0]],
          [[0,0,1],[0,0,1],[1,1,1]]]

# numbers = np.loadtxt("numbers.csv",dtype="int",delimiter=',')
def make_numbers(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns

numbers = []
while len(numbers)<=100:
  number = make_numbers(0,11,12)
  if not number in numbers:
    numbers.append(list(number))

def culclate(result,result_pzl,number,flag):
  global try_count
  global success_stock
  try_count+=1
  # 全てのマスが１で埋まった場合,成功
  if min(list(map(lambda x: min(x), result)))==1:
    if not result_pzl in success_stock:
      print("------succsess---------")
      print(pd.DataFrame(result_pzl))
      print("-----------------------")
      success_stock.append(result_pzl)
    return 0
  else:
    for puz_i in number:
      if flag==True:
        # パズルを順に動かす
        for row_f in range(10-len(puzzle[puz_i])+1):
          for col_f in range(6-len(puzzle[puz_i][0])+1):
            hako = [[0]*6 for i in range(10)]
            # hakoにパズルを入れる
            col = len(puzzle[puz_i][0])
            for row in range(len(puzzle[puz_i])):
              hako[row_f+row][col_f:col_f+col] = puzzle[puz_i][row]
            result_kari = list(map(lambda x,y: list(map(lambda a,b: a+b, x,y)), result, hako))
            # resultとhakoを比較
            if max(list(map(lambda x: max(x), result_kari))) <= 1:
              result = list(map(lambda x,y: list(map(lambda a,b: a+b, x,y)), result, hako))
              result_pzl = list(map(lambda x,y: list(map(lambda a,b: a+b*(puz_i+1), x,y)), result_pzl, hako))
              number.remove(puz_i)
              # 無理ならreturn 0
              culclate(result,result_pzl,number,flag)
              break
          else:
            continue
          break
        flag=False
      else:
        return 0

try_count = 0
success_stock = []

for number in numbers:
  culclate(result,result_pzl,number,flag=True)
print("試行回数：",try_count)