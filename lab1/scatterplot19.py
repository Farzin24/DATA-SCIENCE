import matplotlib.pyplot as plt

# Data
rollnos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
marks = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

# Create scatter plot
plt.scatter(rollnos, marks, color='blue', marker='o', s=80, edgecolors='black')

# Add labels and title
plt.xlabel("Roll Numbers")
plt.ylabel("Marks")
plt.title("Scatterplot of Roll Numbers vs Marks")

# Show grid for better readability
plt.grid(True, linestyle="--", alpha=0.6)

# Display plot
plt.show()

