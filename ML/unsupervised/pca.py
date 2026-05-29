# principle component analysis (PCA)
# it is used to reduce the dimensionality of the data while retaining as much variance as possible
# it give summary of the data in fewer dimensions
# it removes the noise and redundant features from the data

# there are three problems in high dimensional data
#1. model training becomes slower
#2. it becomes difficult to visualize the data
#3. it can lead to overfitting

# dimensionality reduction means reducing the number of features in the data while retaining as much information as possible


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data={
    'age':[25,30,35,40,45,50],
    'income':[50000,60000,70000,80000,90000,100000],
    'spending':[1000,1500,2000,2500,3000,3500],
    'savings':[2000,3000,4000,5000,6000,70000]
    }

df=pd.DataFrame(data)

scaler=StandardScaler()
scaled_data=scaler.fit_transform(df)

pca=PCA(n_components=2)
pca_data=pca.fit_transform(scaled_data)

pca_df=pd.DataFrame(data=pca_data,columns=['Principal Component 1','Principal Component 2'])

explained_variance=pca.explained_variance_ratio_
print("explained variance ratio:")
print(np.round(explained_variance*100,2))

plt.figure(figsize=(8,6))
plt.scatter(pca_df['Principal Component 1'],pca_df['Principal Component 2'],color='blue')
plt.title('PCA of Customer Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid()
plt.show()

print("new data with two principal components:")
print(pca_df)