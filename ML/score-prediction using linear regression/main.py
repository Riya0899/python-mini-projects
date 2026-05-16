import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
import matplotlib.pyplot as plt
import numpy as np

# load dataset
data=pd.read_csv("ML/score-prediction/Students_Grading_Dataset_Biased.csv")

# input and output
x=data[["Study_Hours_per_Week"]]
y=data[["Final_Score"]]

# train model
model=LinearRegression()
model.fit(x,y)
predicted_score=model.predict(x)

# valid regression metrices

mae=mean_absolute_error(y,predicted_score)
mse=mean_squared_error(y,predicted_score)
rmse=np.sqrt(mse)
r2=r2_score(y,predicted_score)

# show results 
print("mean absolute error:",round(mae,2))
print("mean squared error:",round(mse,2))
print("root mean squared error:",round(rmse,2))
print("R-squared(Model Accuracy):",round(r2,4))  # closer to 1 means better fit 

# histogram

plt.figure(figsize=(10,5))
plt.hist(data["Final_Score"], bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("number of students")
plt.grid(True)
plt.show()

# scatter plot + regression line

plt.figure(figsize=(10,5))
plt.scatter(x, y, color="blue", alpha=0.5, label="Actual Scores")
plt.plot(x, predicted_score, color="red", linewidth=2, label="Regression Line")
plt.title("Scatter Plot of Final Scores")
plt.xlabel("model predicted vs actual score")
plt.ylabel("Final Score")
plt.legend()
plt.grid(True)
plt.show()


