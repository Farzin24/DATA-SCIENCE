# count_lines.py

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print("Total number of lines:", len(lines))
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

