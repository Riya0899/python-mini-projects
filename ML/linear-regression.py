'''
linear regression
finds patterns in old data
generates a straight line 
line predicts the future value 
y=mx+b

1. its not about the line,it is about the story
2. 5 rows use start
3. accuracy is not always the goal

'''

from sklearn.linear_model import LinearRegression
x=[[1],[2],[3],[4],[5]]
y=[40,50,65,75,90]

model=LinearRegression()

hours=float(input("enter hoe many hours you studied:"))
model.fit(x,y)
predicted_marks=model.predict([[hours]])
print(f"based on hours {hours} , your predicted marks are: {predicted_marks}")