import numpy as np
import pandas as pd

with open('result2.txt','r') as f:
  texts = f.read()
  texts = texts.replace("-","").replace("[","").replace("]","")
  texts = texts.splitlines()[:-1]
  texts = [text for text in texts if text[:2]!="No" and text!=""]
result = []
results = []
for i,text in enumerate(texts):
  text = list(filter(None, text.split(" ")))
  result.append(text)
  if (i+1)%10==0:
    results.append(result)
    result = []

stock = []
answer = []
for result in results:
  if result not in stock:
    answer.append(result)
    for i in range(4):
      stock.append(result)
      result = np.rot90(np.rot90(result)).tolist()
      if i==1:
        result = np.flipud(result).tolist()

for i,ans in enumerate(answer):
  print("No.",i+1)
  print(np.array(ans))