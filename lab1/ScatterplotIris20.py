import pandas as pd
import matplotlib.pyplot as plt

file_path = input("Enter path to iris CSV file: ")
df = pd.read_csv(file_path)

plt.scatter(df['sepal_length'], df['sepal_width'], color='blue')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Width")
plt.grid(True)
plt.show()
