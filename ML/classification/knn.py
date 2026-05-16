'''
1. chose k value (always odd number to avoid tie)
2. find nearest neighbours
3. count how many are in each class
4. assign the class with the most neighbours
'''
from sklearn.neighbors import KNeighborsClassifier
x=[
    [180,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]  

# 0-> apple 1-> orange
y=[0,0,0,1,1,1]

model=KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
weight=float(input("enter weight of the fruit in gms:"))
size=float(input("enter size of the fruit in cm:"))

prediction=model.predict([[weight,size]])[0]  # without [0] it will return an array with one element, we want the element itself so we use [0]

if prediction==0:
    print("this is likely an apple")
else:
    print("this is likely an orange")
