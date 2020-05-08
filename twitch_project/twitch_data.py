#!/usr/bin/env python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df_stream = pd.read_csv("csv-data/stream.csv")
df_chat = pd.read_csv("csv-data/chat.csv")

print(df_stream.head(10))
print(df_chat.head(10))