#!/usr/bin/env python
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')
df['Total_Goals'] = df['Home Team Goals'] + df['Away Team Goals']
# sns.barplot(data = df, x="Year", y="Total_Goals", estimator=np.sum, ci=None)

sns.set_style("whitegrid")
sns.set_context("poster", font_scale=0.3)


f, ax = plt.subplots(figsize=(12,7))

ax = sns.barplot(data = df, x="Year", y="Total_Goals", estimator=np.sum, ci=None)
ax.set_title("Goals per WorldCup")


goals_per_world_cup = df.groupby(['Year']).Total_Goals.sum().reset_index()

# x_val = range(len(goals_per_world_cup))

# ax = plt.subplot()

# ax.set_xticks(x_val)
# ax.set_xticklabels(goals_per_world_cup['Year'])
# plt.bar(x_val, goals_per_world_cup['Total_Goals'])

f, ax2 = plt.subplots(figsize=(12,7))
sns.set_palette("Spectral")
sns.boxplot(data = df_goals, x="year", y="goals")
plt.title("Goal distribution")


# print(goals_per_world_cup)
# print(df_goals.head())

plt.show()