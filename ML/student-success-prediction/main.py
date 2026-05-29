import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# understanding the data

df=pd.read_csv("ML/student-success-prediction/student_success_dataset.csv")
print("sample rows")
print(df.head())

print("dataset shape")
print(f"rows: {df.shape[0]}, columns: {df.shape[1]}")

print("dataset info")
print(df.info())

print("statistical summary")
print(df.describe(include='all'))



# preprocessing the data

print("missing values")
print(df.isnull().sum())
  
  # for smaller number of text data conversion to number use label encoder
  # for larger number of text data use get dummies 
le=LabelEncoder()
df['Internet']=le.fit_transform(df['Internet'])
df['Passed']=le.fit_transform(df['Passed'])

print("after encoding")
print(df.head())
print("datatypes after encoding")
print(df.dtypes)

# feature scaling

features=['StudyHours','Attendance','Internet','PastScore','SleepHours']
scaler=StandardScaler()
df_scaled=df.copy()
df_scaled[features]=scaler.fit_transform(df[features])


# model training
x=df_scaled[features] # features
y=df_scaled['Passed'] # target variable

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

# model evaluation
print("classification report")
print(classification_report(y_test,y_pred))

print("confusion matrix")
print(confusion_matrix(y_test,y_pred))

# visualizations

plt.figure(figsize=(10,6))
sns.heatmap(confusion_matrix(y_test,y_pred),annot=True,fmt='d',cmap='Blues',xticklabels=['Not Passed','Passed'],yticklabels=['Not Passed','Passed'])

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()

print("---------predict your result-----------")

try:
  study_hours=float(input("enter study hours per week:"))
  attendance=float(input("enter attendance percentage:"))
  internet=float(input("do you have internet access at home? (1 for yes, 0 for no):"))
  past_score=float(input("enter past score percentage:"))
  sleep_hours=float(input("enter sleep hours per day:"))
  
  user_input=pd.DataFrame({
    'StudyHours':[study_hours],
    'Attendance':[attendance],
    'Internet':[internet],
    'PastScore':[past_score],
    'SleepHours':[sleep_hours]
  })
  
  user_input_scaled = pd.DataFrame(
      scaler.transform(user_input),
      columns=features
  )

  prediction = model.predict(user_input_scaled)[0]
  
  result="Passed" if prediction==1 else "Not Passed"
  print(f"the model predicts that you will likely: {result}")
except Exception as e:
  print("invalid input. please enter numeric values.")