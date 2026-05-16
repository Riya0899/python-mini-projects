'''
is fever>100
    yes>cold
        yes>flu
            no>maybe
    no-no flu
    
'''
from sklearn.tree import DecisionTreeClassifier
x=[
    [7,2],  # apple
    [8,3],  # apple
    [9,8],  # orange
    [10,9]  # orange
]
y=[0,0,1,1]

model=DecisionTreeClassifier()
model.fit(x,y)

size=float(input("enter size of the fruit in gms:"))
colorshade=float(input("enter color shade of the fruit (0-10):"))

result=model.predict([[size,colorshade]])[0]
if result==0:
    print("this is likely an apple")
else:
    print("this is likely an orange")


# overfitting- when the model learns the training data too well and performs poorly on unseen data
# underfitting- when the model is too simple to capture the underlying pattern in the data and performs poorly on both training and unseen data
# perfect fit- when the model captures the underlying pattern in the data and performs well on both training and unseen data