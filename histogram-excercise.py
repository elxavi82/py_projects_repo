#!/usr/bin/env python
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])
def count_days(min, max, array):
    count = 0
    day_range = range(min, max+1)
    for element in array:
        for day in day_range:
            if day == element:
                count+=1
    return count




# Count the values in each bin 
days_old_012 = count_days(0,2, days_old_bread)
days_old_345 = count_days(3,5, days_old_bread)
days_old_678 = count_days(6,8, days_old_bread)

# Printing the values
print("Between 0 and 2 days: " + str(days_old_012))
print("Between 3 and 5 days: " + str(days_old_345))
print("Between 6 and 8 days: " + str(days_old_678))