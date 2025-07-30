# find_11_lines.py

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        print("\nLines containing '11':\n")
        for line in file:
            if '11' in line:
                print(line.strip())
except FileNotFoundError:
    print("File not found. Please check the name and try again.")

