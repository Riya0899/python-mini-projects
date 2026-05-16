from sklearn.linear_model import LogisticRegression

x=[[1],[2],[3],[4],[5]]  # hours of study
y=[0,0,1,1,1]  # pass (0) or fail (1) -> label for classification

model=LogisticRegression()
model.fit(x,y)

hours=float(input("enter how many hours you studied:"))
result=model.predict([[hours]])[0]

if result==1:
    print(f"based on hours {hours} , you are predicted to pass the exam.")
else:
    print(f"based on hours {hours} , you are predicted to fail the exam.")