# Get file names from user
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    # Open source file in read mode and destination in write mode
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        # Copy contents
        for line in src:
            dest.write(line)

    print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")

except FileNotFoundError:
    print("Source file not found. Please check the file name and try again.")

