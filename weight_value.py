#!/usr/bin/env python
import numpy as np

def weight_val(data_val):
    return np.repeat(1.0/len(data_val), len(data_val))


           