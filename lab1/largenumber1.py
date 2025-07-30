# Get list of numbers from the user
numbers = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
num_list = [int(num) for num in numbers.split()]

# Find the largest number
largest = max(num_list)

# Display the result
print("The largest number is:", largest)

