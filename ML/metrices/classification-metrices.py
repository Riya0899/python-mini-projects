'''
1. accuracy - percentage of total corrected predictions 
accuracy=correct pred/total pred

2.precision- percentage of correct positive predictions out of all positive predictions

3.recall= percentage of correct positive predictions out of all actual positives

4. f1 score- harmonic mean of precision and recall
'''  

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
# true answers
y_true=[1,0,1,1,0,1,0]

# predicted answers
y_pred=[1,0,1,0,0,1,1]

# evaluation
print("accuracy:",accuracy_score(y_true,y_pred))
print("precision:",precision_score(y_true,y_pred))
print("recall:",recall_score(y_true,y_pred))
print("f1 score:",f1_score(y_true,y_pred))
