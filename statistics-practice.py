#!/usr/bin/env python
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction data to numpy arrays
#times1 = transactions["Transaction Time"]
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Find the minimum time, maximum time, and range
min_time = np.amin(times)
max_time = np.amax(times) # <-- Replace with max calc
range_time = 0 # <-- Replace max - min

# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))