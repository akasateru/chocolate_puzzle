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

def culclate(stock):
  if len(stock)==12:
    return 0
  else:
    for puz_i in range(12):
      if not puz_i in stock:
        stock.append(puz_i)
        print(stock)
        culclate(stock)


culclate(stock=[])



