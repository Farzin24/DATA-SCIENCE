# Get input from user
user_input = input("Enter numbers separated by spaces: ")

# Convert to list of integers
numbers = [int(num) for num in user_input.split()]

# Remove duplicates while preserving order
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Print result
print("List without duplicates:", unique_numbers)

