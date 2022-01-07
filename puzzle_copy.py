from numpy.core.fromnumeric import nonzero
import pandas as pd
import numpy as np
import time

start = time.time()



puzzles_moto = [[[1,1,1,1,1]],
          [[0,2],[2,2],[2,2]],
          [[3,3,3],[0,3,0],[0,3,0]],
          [[0,4,0],[4,4,0],[0,4,4]],
          [[5,0],[5,0],[5,0],[5,5]],
          [[0,6,0],[6,6,6],[0,6,0]],
          [[0,0,7],[0,7,7],[7,7,0]],
          [[0,0,8],[8,8,8],[8,0,0]],
          [[9,9,9],[9,0,0],[9,0,0]],
          [[10,10,0,0],[0,10,10,10]],
          [[11,11],[0,11],[11,11]],
          [[0,12,0,0],[12,12,12,12]]]
          
puzzles_moto = [[[1,1,1],[1,0,1]],
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

puzzles = []
for puzzle_moto in puzzles_moto:
  puzzle = []
  for turn in range(8):
    if puzzle_moto not in puzzle:
      puzzle.append(puzzle_moto)
    puzzle_moto = np.rot90(puzzle_moto).tolist()
    if turn==3:
      puzzle_moto = np.flipud(puzzle_moto).tolist()
  puzzles.append(puzzle)

result_stock = []

def culclate(result,puzzles,lv,stock):
  global try_count
  try_count+=1
  lv+=1
  # 全てのマスが１で埋まった場合,成功
  if result.min() != 0:
    global result_stock
    if result.tolist() not in result_stock:
      print("------success---------")
      print(pd.DataFrame(result))
      print("-----------------------")
      result_stock.append(result.tolist())
      return 0
  else:
    for i in range(10):
      if result[9-i].min() != 0:
        if len(puzzles)*5 != np.count_nonzero(result[9-i+1:]==0):
          return 0
        break
    for i in range(10):
      if np.array(result[i]).min() == 0:
        r = i
        break

    for i,puzzle in enumerate(puzzles):
      for puz in puzzle:
        row = len(puz)
        col = len(puz[0])
        flag = True
        if r < 11-row:
          for row_f in range(r,11-row):
            for col_f in range(7-col):
              if (result[row_f:row_f+row,col_f:col_f+col]*puz).max() == 0:
                result_next = np.array(result)
                result_next[row_f:row_f+row,col_f:col_f+col] += puz
                # はめたパズルをリストから抜く
                puzzles_next = np.delete(puzzles,i,axis=0)
                # 確認用
                stock_next = stock[::]
                stock_next.append(np.array(puz).max())
                print(stock_next)
                # 再帰
                culclate(result_next,puzzles_next,lv,stock_next)
                flag = False
                break
            if flag==False:
              break
    return 0

result = np.array([[0]*6 for i in range(10)])
lv = 0
try_count = 0
stock = []
culclate(result,puzzles,lv,stock)

end = time.time() - start
print(f"{end:3f}s")