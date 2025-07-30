import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode

path = input("Enter path to iris CSV file: ")
df = pd.read_csv(path)

X = df.iloc[:, :-1].values
true_labels = df.iloc[:, -1].values

kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X)

# Map clusters to actual species by majority voting
labels = []
for i in range(3):
    mask = (clusters == i)
    labels.append(mode(true_labels[mask]).mode[0])

predicted = [labels[c] for c in clusters]
print("Clustering accuracy vs true species:", accuracy_score(true_labels, predicted))
