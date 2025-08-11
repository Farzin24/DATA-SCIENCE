import matplotlib.pyplot as plt

rollnos = list(map(int, input("Enter roll numbers: ").split()))
marks = list(map(int, input("Enter marks: ").split()))

plt.scatter(rollnos, marks, color='red')
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Roll Number vs Marks")
plt.grid(True)
plt.show()
