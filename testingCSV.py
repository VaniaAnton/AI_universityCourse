import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# # Reading Data And Apply EDA
df = pd.read_csv('data.csv')

# # Data Representation
df['Match'] = df['HomeTeam'] + ' vs ' + df['AwayTeam']

#print the head of file
print(df.head())

#print the tail of file
# print(df.tail(3))

#prints information about the DataFrame
# print(df.info())

# quick overview of my data
# print(df.describe())

# count the number of duplicated files 
# print(df.duplicated().sum())

# returns the total number of NaN values in the entire DataFrame
# print(df.isna().sum())

# Top 10 Home Teams with figure
# print(df['HomeTeam'].value_counts().head(10))
# plt.figure(figsize=(10, 6))
# sns.barplot(x=df['HomeTeam'].value_counts().head(10).index,
#             y=df['HomeTeam'].value_counts().head(10).values,
#             palette='pastel',
#         )
# plt.xlabel('Club')
# plt.ylabel('Number of matches')
# plt.title('Top 10 Home Teams')
# plt.xticks(rotation=45)
# plt.show()

# Top 10 Away Teams
# print(df['AwayTeam'].value_counts().head(10))
# plt.figure(figsize=(10, 6))
# sns.barplot(
#     x=df['AwayTeam'].value_counts().head(10).index, 
#     y=df['AwayTeam'].value_counts().head(10).values, 
#     palette='pastel', 
# )
# plt.xlabel('Club')
# plt.ylabel('Number of matches')
# plt.title('Top 10 Away Teams')
# plt.xticks(rotation=45)
# plt.show()

# Full Time Home Goals count, average and plot
# print(df['FTH Goals'].describe())
# Full_Time_Home_Goals = df['FTH Goals'].value_counts().reset_index()
# print(Full_Time_Home_Goals)
# plt.figure(figsize=(10, 6))
# sns.barplot(x=Full_Time_Home_Goals['FTH Goals'], y=Full_Time_Home_Goals['count'], data=Full_Time_Home_Goals, palette='pastel')
# plt.ylabel('Num of Goals')
# plt.title('Full Time Home Goals')
# plt.show()

# Full Time Away Goals
# print(df['FTA Goals'].describe())
# Full_Time_Home_Goals = df['FTA Goals'].value_counts().reset_index()
# print(Full_Time_Home_Goals)
# plt.figure(figsize=(10, 6))
# sns.barplot(x=Full_Time_Home_Goals['FTA Goals'], y=Full_Time_Home_Goals['count'], data=Full_Time_Home_Goals, palette='pastel')
# plt.ylabel('Num of Goals')
# plt.title('Full Time Away Goals')
# plt.show()

# Top 5 Matches with Highest Total Goals
# df['TotalGoals'] = df['FTH Goals'] + df['FTA Goals']
# top_goal_matches = df.nlargest(10, 'TotalGoals')
# print(top_goal_matches)
# fig, ax = plt.subplots(figsize=(11, 8))
# sns.barplot(x='TotalGoals', y='Match', data=top_goal_matches, palette='coolwarm', ax=ax)
# for index, value in enumerate(top_goal_matches['TotalGoals']):
#     ax.text(value + 0.2, index, str(value), va='center', fontsize=12, fontweight='bold')
# plt.xlabel('Total Goals')
# plt.ylabel('Match')
# plt.title('Top 5 Matches with Highest Total Goals')
# plt.show()

# Full-Time Result Percentage
# FT_Result_Percentage = df['FT Result'].value_counts(normalize=True).reset_index()
# FT_Result_Percentage.columns = ['FT Result', 'Percentage']
# FT_Result_Percentage['Percentage'] *= 100
# print(FT_Result_Percentage)
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(x='Percentage', y='FT Result', data=FT_Result_Percentage, palette='pastel', ax=ax)
# for index, value in enumerate(FT_Result_Percentage['Percentage']):
#     ax.text(value + 0.5, index, f"{value:.1f}%", va='center', fontsize=12, fontweight='bold')
# plt.xlabel('Percentage (%)')
# plt.ylabel('Full-Time Result')
# plt.title('Full-Time Result Percentage')
# plt.show()

# Top 10 Clean Matches (No Red Cards)
# top_clean_matches = df[(df['A Red'] == 0) & (df['H Red'] == 0)]['Match'].value_counts().head(10).reset_index()
# top_clean_matches.columns = ['Match', 'Count']
# print(top_clean_matches)
# plt.figure(figsize=(10, 6))
# ax = sns.barplot(x='Count', y='Match', data=top_clean_matches, palette='pastel')

# for index, value in enumerate(top_clean_matches['Count']):
#     ax.text(value + 0.2, index, str(value), va='center', fontsize=12, fontweight='bold')

# plt.xlabel('Number of Matches')
# plt.ylabel('Match')
# plt.title('Top 10 Clean Matches (No Red Cards)')
# plt.show()


