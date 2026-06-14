from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

df=sns.load_dataset('iris')
print(df.head())

X = df.drop('species', axis=1)
y = df['species']

le=LabelEncoder()
y_encoded=le.fit_transform(y)
 
# stacking
X_train, X_test, y_train, y_test=train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)
base_learners=[
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('svc', SVC(probability=True, kernel='rbf', random_state=42)),
    ('lr', LogisticRegression(max_iter=1000))
]

meta_learner=LogisticRegression(max_iter=1000)

stacking_clf = StackingClassifier(
    estimators=base_learners,
    final_estimator=meta_learner,
    cv=5
)

stacking_clf.fit(X_train, y_train)
y_pred=stacking_clf.predict(X_test)
accuracy=accuracy_score(y_test, y_pred)
print("Stacking: ",round(accuracy,3))


# bagging

rf_model=RandomForestClassifier(
    n_estimators=100, #no. of trees
    max_depth=None, #let trees grow fully
    random_state=42
)

rf_model.fit(X_train, y_train)
y_pred1=rf_model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred1)
print("Random Forest: ",round(accuracy,3))


# boosting

ada_model=AdaBoostClassifier(n_estimators=100, random_state=42)
ada_model.fit(X_train, y_train)
y_pred2=ada_model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred2)
print("Ada Boost: ",round(accuracy,3))

grad_model=GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
grad_model.fit(X_train, y_train)
y_pred3=grad_model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred3)
print("Gradient Boosting: ",round(accuracy,3))

xg_model=XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3,
             eval_metric='mlogloss')
xg_model.fit(X_train, y_train)
y_pred4=xg_model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred4)
print("XG Boost: ",round(accuracy,3))


