import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset (from seaborn or a CSV)
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Check available columns
# print(df.columns)

# Plot histogram for Sepal Length
plt.hist(df['sepal length (cm)'], bins=10, color='lavender', edgecolor='black')
plt.title('Histogram of Sepal Length (Iris Dataset)')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

