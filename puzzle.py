import pandas as pd
import numpy as np
import time

success = [[1]*10 for i in range(6)]
result = [[0]*10 for i in range(6)]
result_pzl = [[0]*10 for i in range(6)]

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

def culclate(result,result_pzl,number,i,flag,run_once):
  i+=1
  print("\n深さ:",i)
  if number==[] and min(list(map(lambda x: min(x), result)))==1:
    print("------succsess---------")
    print(pd.DataFrame(result_pzl))
    print("-----------------------")
    return 0
  else:
    for puz_i in number:
      if flag==True:
        # hakoを順に動かす
        for row_f in range(6-len(puzzle[puz_i])+1):
          for col_f in range(10-len(puzzle[puz_i][0])+1):
            hako = [[0]*10 for i in range(6)]
            hako_pzl = [[0]*10 for i in range(6)]
            # hakoにパズルを入れる
            for row in range(len(puzzle[puz_i])):
              for col in range(len(puzzle[puz_i][0])):
                hako[row_f+row][col_f+col] = puzzle[puz_i][row][col]
                if puzzle[puz_i][row][col] == 1:
                  hako_pzl[row_f+row][col_f+col] = puz_i+1
            result_kari = list(map(lambda x,y: list(map(lambda a,b: a+b, x,y)), result, hako))
            # resultとhakoを比較
            if max(list(map(lambda x: max(x), result_kari))) <= 1:
              result = list(map(lambda x,y: list(map(lambda a,b: a+b, x,y)), result, hako))
              result_pzl = list(map(lambda x,y: list(map(lambda a,b: a+b, x,y)), result_pzl, hako_pzl))
              number.remove(puz_i)
              print("result_pzl:\n",pd.DataFrame(result_pzl))
              print("number:",number)
              culclate(result,result_pzl,number,i,flag,run_once)
              break
            if row_f+row==5 and col_f+col==9 and max(list(map(lambda x: max(x), result_kari))) > 1:
              print("\n--------fault---------")
              run_once=1
              return 0
          else:
            continue
          break
        flag=False
      else:
        return 0

number1 = [0,1,2,3,4,5,6,7,8,9,10,11]
number2 = [1,2,3,4,5,6,7,8,9,10,11,0]
number3 = [2,3,4,5,6,7,8,9,10,11,0,1]

culclate(result,result_pzl,number1,i=0,flag=True,run_once=0)