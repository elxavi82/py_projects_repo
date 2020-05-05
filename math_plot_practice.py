#!/usr/bin/env python
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
x_val = range(len(years))
plt.axis([-0.5, 6.5, 70, 95])
plt.bar(x_val, past_years_averages, yerr=error)
plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test average")
plt.savefig('my_bar_chart.png')
ax= plt.subplot()
ax.set_xticks(x_val)
ax.set_xticklabels(years)
plt.show()
