import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

df=sns.load_dataset('iris')
print(df.head())
print(df['species'].unique())

X = df.drop('species', axis=1)
y = df['species']

X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train, y_train)
print(model_knn.score(X_test, y_test))

model_svm = SVC(gamma='auto')
model_svm.fit(X_train, y_train)
print(model_svm.score(X_test, y_test))

#now lets use grid search CV
from sklearn.model_selection import GridSearchCV
classifier = GridSearchCV((model_svm),{
    'C' : [1,10,20,30],
    'kernel' : ['rbf', 'linear'],
}, cv=5, return_train_score=False)

classifier.fit(X, y)
results=pd.DataFrame(classifier.cv_results_)
print(results[['param_C', 'param_kernel', 'mean_test_score']])

#randomized search CV
from sklearn.model_selection import RandomizedSearchCV
classifier_r = RandomizedSearchCV((model_svm),{
    'C' : [1,10,20,30],
    'kernel' : ['rbf', 'linear'],
},n_iter=4, cv=5, return_train_score=False)

classifier_r.fit(X, y)
results=pd.DataFrame(classifier_r.cv_results_)
print(results[['param_C', 'param_kernel', 'mean_test_score']])