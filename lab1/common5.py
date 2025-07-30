list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()

# Check for common elements
common = False
for item in list1:
    if item in list2:
        common = True
        break

print("Do they have at least one common member?", common)

