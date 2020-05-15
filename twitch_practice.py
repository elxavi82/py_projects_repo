#!/usr/bin/env python
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

x_val = range(len(games))

# plt.bar(x_val, viewers, color='red')
# ax = plt.subplot()
# ax.set_xticks(x_val)
# ax.set_xticklabels(games, rotation=25)
# plt.title("Number of Viewers per Game")
# plt.legend('Twitch')
# plt.xlabel("Games")
# plt.ylabel("Viewers")

y_upper = [(element*0.15) + element for element in viewers_hour]

y_lower = [element - (element*0.15) for element in viewers_hour]
plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.show()