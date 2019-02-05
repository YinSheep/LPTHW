from sys import argv

# Set two input variables, one is script name, one is filename
script, filename = argv

# Open the corresponding text file
txt = open(filename)

# Print a sentence
print(f"Here's your file {filename}:")
# Print out the content of the text file
print(txt.read())

txt.close()

# Instructs you to type another filename
print("Type the filename again:")
# The user input the filename here
file_again = input("> ")

# Open the corresponding text file
txt_again = open(file_again)

# Print out the content of the text file
print(txt_again.read())

txt_again.close()
