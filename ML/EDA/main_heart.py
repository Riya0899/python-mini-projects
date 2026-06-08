# train a model to predict heart disease

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("ML/EDA/heart.csv")
# print(df.head())

# EDA

# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df.describe())
print(df.duplicated().sum())
print(df['HeartDisease'].value_counts())
print(df.isnull().sum())

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

def plotting(var, ax):
    sns.histplot(df[var], kde=True, ax=ax)
    ax.set_title(var)

plotting('Age', axes[0, 0])
plotting('RestingBP', axes[0, 1])
plotting('Cholesterol', axes[1, 0])
plotting('MaxHR', axes[1, 1])

plt.tight_layout()
# plt.show()

# mostly cholestrol have zero values which is not possible, so we will replace those with mean value of cholestrol
# similarly for resting blood pressure, we will replace zero values with mean value of resting blood pressure
ch_mean=df.loc[df['Cholesterol']!=0, 'Cholesterol'].mean()
# print(f"Mean Cholesterol (excluding zeros): {ch_mean}")
df['Cholesterol']=df['Cholesterol'].replace(0, ch_mean)
df['Cholesterol']=df['Cholesterol'].round(2)

df['RestingBP']=df['RestingBP'].replace(0, df['RestingBP'].mean())
df['RestingBP']=df['RestingBP'].round(2)

sns.countplot(x = df['Sex'], hue= df['HeartDisease'])
# plt.show()

# sns.countplot(x = df['ChestPainType'], hue= df['HeartDisease'])
# plt.show()

# sns.countplot(x = df['FastingBS'], hue= df['HeartDisease'])
# plt.show()

# sns.boxplot(x = 'HeartDisease', y = 'Cholesterol', data=df)
# plt.show()

# sns.violinplot(x = 'HeartDisease', y = 'Age', data=df)
# plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

#DATA PREPROCESSING
df_encode=pd.get_dummies(df, drop_first=False)
print(df_encode.astype(int))

from sklearn.preprocessing import StandardScaler
numerical_cols=['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
scaler=StandardScaler()
df_encode[numerical_cols]=scaler.fit_transform(df_encode[numerical_cols])
print(df_encode.head())

