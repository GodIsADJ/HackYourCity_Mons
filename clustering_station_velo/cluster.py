import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('coordinate_event_lat_lon.csv', error_bad_lines=False)
df = df.dropna() 

x = df['latitude']
y = df['longitude']



data_set = np.dstack((x,y))
data_set = data_set[0]
kmeans = KMeans(4).fit(data_set)

print(kmeans.cluster_centers_)

centroids = kmeans.cluster_centers_
print(centroids)

df['cluster']=kmeans.labels_

c1_df = df[df["cluster"] == 0]
c2_df = df[df["cluster"] == 1]
c3_df = df[df["cluster"] == 2]
c4_df = df[df["cluster"] == 3]



plt.scatter(x=c1_df['latitude'], y=c1_df['longitude'], c='green', s=50, alpha=0.5)
plt.scatter(x=c2_df['latitude'], y=c2_df['longitude'], c='red', s=50, alpha=0.5)
plt.scatter(x=c3_df['latitude'], y=c3_df['longitude'], c='blue', s=50, alpha=0.5)
plt.scatter(x=c4_df['latitude'], y=c4_df['longitude'], c='black', s=50, alpha=0.5)




#create centroides 

plt.scatter(50.45871144, 3.95662095, c='yellow',norm=1)
plt.scatter(50.45505764, 3.95287386, c='yellow',norm=1)
plt.scatter(50.45535941, 3.95968002, c='yellow',norm=1)
plt.scatter(50.45144295, 3.94943058, c='yellow',norm=1)



plt.show()
