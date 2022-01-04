import pandas as pd
import numpy as np
          
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

def culclate():
  global stock
  global try_count
  global success_stock
  global result
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
    # 12ピースを埋めていく
    for puz_i in range(12):
      if puz_i not in stock:
        print("puz_i:",puz_i)
        # ピースを回す
        # ピースを左上から順に動かす
        print(pd.DataFrame(puzzle[puz_i]))
        flag = True
        for row_f in range(10-len(puzzle[puz_i])+1):
          if flag==True:
            for col_f in range(6-len(puzzle[puz_i][0])+1):
              row = len(puzzle[puz_i])
              col = len(puzzle[puz_i][0])
              result_kari = np.array(result)[row_f:row_f+row, col_f:col_f+col]
              # resultと被っていなければ、ピースを埋める
              if (result_kari*puzzle[puz_i]).max() == 0:
                result[row_f:row_f+row,col_f:col_f+col] += puzzle[puz_i]
                stock.append(puz_i)
                print("success")
                print("stock:",stock)
                print(pd.DataFrame(result),"\n")
                culclate()
                flag = False
                break
              elif row_f+row==10 and col_f+col==6:
                result = np.where(result==stock[-1]+1,0,result)
                stock.pop(-1)
                print("fault")
                print("stock:",stock)
                print(pd.DataFrame(result),"\n")
                return 0
          else:
            break
    result = np.where(result==stock[-1]+1,0,result)
    stock.pop(-1)
    return 0


        

try_count = 0
result = np.array([[0]*6 for i in range(10)])
success_stock = []
stock = []

culclate()
print("試行回数:",try_count)