# density based algorithm
# non parameteric algo
# epsilon distance

from sklearn.datasets import make_moons
from sklearn.cluster import KMeans,DBSCAN
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# kmeans 

X,y_true=make_moons(n_samples=500,noise=0.05,random_state=42)
df = pd.DataFrame(X, columns=['Feature_1', 'Feature_2'])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

kmeans=KMeans(n_clusters=2, random_state=42)
kmeans_labels=kmeans.fit_predict(X_scaled)
 
df['kmeans_cluster']=kmeans_labels 
sns.scatterplot(x=df['Feature_1'],y=df['Feature_2'],hue=df['kmeans_cluster'])
palette='tab10'

# dbscan

dbscan=DBSCAN(eps=0.3,min_samples=5) 
dbscan_labels=dbscan.fit_predict(X_scaled)

df['dbscan_cluster']=dbscan_labels
sns.scatterplot(x=df['Feature_1'],y=df['Feature_2'],hue=df['dbscan_cluster'])
palette='tab10'



