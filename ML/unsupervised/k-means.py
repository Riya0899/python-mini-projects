import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# sample data
data={
    'customer':['riya','aman','faizan','neha','imran','sneha'],
    'age':[25,30,35,40,45,50],
    'spending':[1000,1500,2000,2500,3000,3500]
       
}

df=pd.DataFrame(data)
x=df[['age','spending']]

model=KMeans(n_clusters=2,random_state=42,n_init=10)
df['group']=model.fit_predict(x)

plt.figure(figsize=(6,5))
for group in df['group'].unique():  # unique gives distinct values in the group column
    group_data=df[df['group']==group]  # masking
    plt.scatter(group_data['age'],group_data['spending'],label=f'Group {group}')

plt.xlabel('Age')
plt.ylabel('Spending')
plt.title('Customer Segmentation (k-means)')
plt.grid()
plt.legend()
plt.show()