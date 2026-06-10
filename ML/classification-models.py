import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df=sns.load_dataset("titanic")
print(df.head())
# print(df.info())

df.drop(['deck', 'embark_town', 'alive', 'class', 'who', 'adult_male'], axis=1, inplace=True)
# print(df.info())

df['age'].fillna(df['age'].mean(), inplace=True)
df.dropna(subset=['embarked'], inplace=True)
print(df.info())

le=LabelEncoder()
df['sex']=le.fit_transform(df['sex'])
df['embarked']=le.fit_transform(df['embarked'])
df=df.astype(int)
print(df.head())

X=df.drop('survived', axis=1)
y=df['survived']
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

model=LogisticRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)

print("----LOGISTIC REGRESSION----")
print("Accuracy : ",accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

scaler=StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

knn_model=KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)
y_pred_knn=knn_model.predict(X_test_scaled)
print("----KNN MODEL----")
print("Accuracy : ",accuracy_score(y_test, y_pred_knn))
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))

naive_model=GaussianNB()
naive_model.fit(X_train,y_train)
y_pred_naive=naive_model.predict(X_test)
print("----NAIVE BAYES----")
print("Accuracy : ",accuracy_score(y_test, y_pred_naive))
print(confusion_matrix(y_test, y_pred_naive))
print(classification_report(y_test, y_pred_naive))

tree_model=DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train_scaled, y_train)
y_pred_tree=tree_model.predict(X_test_scaled)
print("----TREE MODEL----")
print("Accuracy : ",accuracy_score(y_test, y_pred_tree))
print(confusion_matrix(y_test, y_pred_tree))
print(classification_report(y_test, y_pred_tree))

svm_model=SVC(kernel='rbf')
svm_model.fit(X_train_scaled, y_train)
y_pred_svm=svm_model.predict(X_test_scaled)
print("----SVC MODEL----")
print("Accuracy : ",accuracy_score(y_test, y_pred_svm))
print(confusion_matrix(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))


#######################################################################
#CROSS VALIDATION
from sklearn.model_selection import cross_val_score
X=df.drop('survived', axis=1)
y=df['survived']

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

scores=cross_val_score(svm_model, X_scaled, y, cv=5, scoring='accuracy')
print(scores)
print(scores.mean())