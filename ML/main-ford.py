import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df=pd.read_csv("ML/ford.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

#EDA
# sns.histplot(df['price'], bins=50, kde=True)
# plt.show()

# sns.heatmap(df.corr(numeric_only=True), annot=True)
# plt.show()

# sns.boxplot(data=df, x='year', y='price')
# plt.xticks(rotation=90)
# plt.show()

# sns.scatterplot(data=df, x='mileage', y='price')
# plt.show()

# sns.boxplot(data=df,x='engineSize', y='price')
# plt.show()

# sns.boxplot(data=df, x='transmission', y='price')
# plt.show()

# sns.boxplot(data=df, x='fuelType', y='price')
# plt.show()

# sns.boxplot(data=df, x='model', y='price')
# plt.xticks(rotation=90)
# plt.show()

# sns.boxplot(data=df, x='tax', y='price')
# plt.xticks(rotation=90)
# plt.show()

# sns.scatterplot(data=df, x='mpg', y='price')
# plt.show()

X=df.drop(columns=['price'], axis=1)
y=df['price']

X_one_encode=pd.get_dummies(X, columns=['model', 'transmission', 'fuelType'], drop_first=False)
print(X_one_encode.astype(int))

encode=LabelEncoder()
columns=['model', 'transmission', 'fuelType']
Xlabel=X
for i in columns:
    Xlabel[i] = encode.fit_transform(Xlabel[i])
print(Xlabel)

numerical_cols=['year', 'mileage', 'tax', 'mpg', 'engineSize']
scaler=StandardScaler()
X_one_encode[numerical_cols]=scaler.fit_transform(X_one_encode[numerical_cols])

Xlabel[['model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]=scaler.fit_transform(Xlabel[['model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']])

X_train, X_test, y_train, y_test=train_test_split(X_one_encode, y, test_size=0.20, random_state=42)
model=LinearRegression()
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
r2=r2_score(y_test, y_pred)
print(r2)

n=X_test.shape[0]
p=X_test.shape[1]
adjusted_r2= 1 - ((1-r2) * (n-1)/ (n-p-1))
print(adjusted_r2)

X_train, X_test, y_train, y_test=train_test_split(Xlabel, y, test_size=0.20, random_state=42)
model2=LinearRegression()
model2.fit(X_train, y_train)

y_pred=model2.predict(X_test)
r2=r2_score(y_test, y_pred)
print(r2)

n=X_test.shape[0]
p=X_test.shape[1]
adjusted_r2= 1 - ((1-r2) * (n-1)/ (n-p-1))
print(adjusted_r2)