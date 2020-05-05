#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

def y_func(x):
  return 2*x+3

def func(x):
  return 3*x-1


x = list(range(0,15))
y1 = []
y2 = []

for i in x:
  y1.append(y_func(i))
  y2.append(func(i))

plt.axis([0,15,0,20])  
plt.plot(x,y1, color="red", marker="o")
plt.plot(x,y2, color="blue", marker="o")
plt.title("two graphs")
plt.xlabel("Varibale X")
plt.ylabel("f(x)")
plt.legend(["Function 1", "Function 2"])

plt.savefig('linear-func.png')
plt.show()