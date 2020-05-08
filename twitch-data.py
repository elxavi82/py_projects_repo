#!/usr/bin/env python
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df_stream = pd.read_csv('stream.csv')
df_chat = pd.read_csv('chat.csv')

print(df_stream.head(10))
print(df_chat.head(10))