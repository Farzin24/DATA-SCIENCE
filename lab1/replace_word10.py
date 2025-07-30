# replace_word.py

file_name = input("Enter the file name: ")
search_word = input("Enter the word to search: ")
replace_word = input("Enter the replacement word: ")

with open(file_name, 'r') as f:
    content = f.read()

# Replace word
content = content.replace(search_word, replace_word)

with open(file_name, 'w') as f:
    f.write(content)

print("Word replaced successfully.")

