'''
1. true positive{TP}- when the model correctly predicts the positive class
2. true negative{TN}- when the model correctly predicts the negative class
3. false positive{FP}- when the model incorrectly predicts the positive class
4. false negative{FN}- when the model incorrectly predicts the negative class
'''
from sklearn.metrics import confusion_matrix

y_true=[1,0,1,1,0,1,0,0,1,0] # true labels
y_pred=[1,0,1,0,0,1,1,0,1,0] # predicted labels

cm=confusion_matrix(y_true,y_pred)
print("confusion matrix:")
print(cm)

'''
            actual_pass   actual_fail
pred_pass     TP              FP
pred_fail     FN              TN

'''
