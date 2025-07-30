import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode

path = input("Enter path to wisc_bc_data.csv: ")
df = pd.read_csv(path)

X = df.iloc[:, 2:].values  # skip id, diagnosis columns
true_labels = df['diagnosis'].values

kmeans = KMeans(n_clusters=2, random_state=0)
clusters = kmeans.fit_predict(X)

# Map clusters to diagnosis labels
labels = []
for i in range(2):
    mask = (clusters == i)
    labels.append(mode(true_labels[mask]).mode[0])

predicted = [labels[c] for c in clusters]
print("Clustering accuracy vs diagnosis:", accuracy_score(true_labels, predicted))
