import matplotlib.pyplot as plt

marks = list(map(int, input("Enter marks: ").split()))
bins = list(range(0, 101, 10))

plt.hist(marks, bins=bins, edgecolor='black')
plt.xlabel("Marks Range")
plt.ylabel("Count")
plt.title("Histogram of Student Marks")
plt.show()
