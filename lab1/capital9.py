# Get input and output file names from user
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    # Open input file for reading, output file for writing
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line into words, capitalize each, then join back
            capitalized_words = ' '.join([word.upper() for word in line.split()])
            outfile.write(capitalized_words + '\n')

    print(f"Words capitalized and written to '{output_file}' successfully.")

except FileNotFoundError:
    print("Input file not found. Please check the file name and try again.")

