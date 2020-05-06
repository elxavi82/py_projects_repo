#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
plt.figure(figsize=(10,8))
x_val_A = range(len(As))
x_val_B = range(len(Bs))
x_val_C = range(len(Cs))
x_val_D = range(len(Ds))
x_val_F = range(len(Fs))

plt.bar(x_val_A, As)
plt.bar(x_val_B, Bs, bottom = As)
plt.bar(x_val_C, Cs, bottom = c_bottom)
plt.bar(x_val_D, Ds, bottom = d_bottom)
plt.bar(x_val_F, Fs, bottom = f_bottom)
#create d_bottom and f_bottom here
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title("Grade distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")
plt.legend(['A', 'B', 'C', 'D', 'F'])
plt.savefig('my_stacked_bar.png')
plt.show()