# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2TogiJAh9XGKavPMyedyUyLsNNttSBn
"""

import random
n = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(n)

ans = n[0:4]

def check(n):
  A = 0
  B = 0      
  for i in range(4):
    if ans[i]== int(n[i]):
      A+=1
    for j in range(4):
      if i==j:
        continue
      if ans[i]==int(n[j]):
        B+=1        
        
  print("A:",A," B:",B)
  
  if A==4:
    return 1
  return 0

while True:
  strr = input("輸入:")
  length = len(str)
  if length!= 4:
    print("請輸入四個數字")
    continu  
  
  if check(strr)==1:
    print("WIN!!")
    break