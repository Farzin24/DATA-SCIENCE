import matplotlib.pyplot as plt

# Marks data
marks = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

# Define bins for intervals 0-10, 10-20, ..., 90-100
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create histogram
plt.hist(marks, bins=bins, edgecolor='black', color='skyblue')

# Add labels and title
plt.xlabel("Marks Interval")
plt.ylabel("Number of Students")
plt.title("Histogram of Marks")

# Show grid for better clarity
plt.grid(axis='y', linestyle="--", alpha=0.6)

# Display plot
plt.show()

