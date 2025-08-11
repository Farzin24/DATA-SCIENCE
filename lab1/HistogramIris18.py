import pandas as pd
import matplotlib.pyplot as plt

file_path = input("Enter path to iris CSV file: ")
df = pd.read_csv(file_path)

plt.hist(df['sepal_length'], bins=10, edgecolor='black')
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length")
plt.show()
