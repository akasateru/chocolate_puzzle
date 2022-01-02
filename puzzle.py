import pandas as pd
import numpy as np

result = np.array([[0]*6 for i in range(10)])
number = [0,1,2,3,4,5,6,7,8,9,10,11]
          
puzzle = [[[1,1,1],[1,0,1]],
          [[2,2,0],[0,2,2],[0,0,2]],
          [[3,3,0],[0,3,3],[0,3,0]],
          [[4,4,4],[0,4,0],[0,4,0]],
          [[0,5],[5,5],[5,0],[5,0]],
          [[0,6,0],[6,6,6],[0,6,0]],
          [[0,0,0,7],[7,7,7,7]],
          [[8],[8],[8],[8],[8]],
          [[0,9,9],[0,9,0],[9,9,0]],
          [[10,10,0],[10,10,10]],
          [[11,11,11,11],[0,11,0,0]],
          [[0,0,12],[0,0,12],[12,12,12]]]

def culclate(result,number,flag):
  global try_count
  global success_stock
  try_count+=1
  # 全てのマスが１で埋まった場合,成功
  if result.min() != 0:
    if not result in success_stock:
      print("------succsess---------")
      print(pd.DataFrame(result))
      print("-----------------------")
      success_stock.append(result)
    return 0
  else:
    for puz_i in number:
      if flag==True:
        # パズルを順に動かす
        for row_f in range(10-len(puzzle[puz_i])+1):
          for col_f in range(6-len(puzzle[puz_i][0])+1):
            #resultにパズルを入れていく-------------------
            row = len(puzzle[puz_i])
            col = len(puzzle[puz_i][0])
            result_kari = np.array(result)[row_f:row_f+row, col_f:col_f+col]
            if (result_kari*puzzle[puz_i]).max() == 0:
              result = np.array(result)
              result[row_f:row_f+row,col_f:col_f+col] += puzzle[puz_i]
              number.remove(puz_i)
              culclate(result,number,flag)
              break
          else:
            continue
          break
        flag=False
      else:
        return 0

try_count = 0
success_stock = []
culclate(result,number,flag=True)
print("試行回数：",try_count)