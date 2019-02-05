# Instructs you to type another filename
print("Type the filename again:")
# The user input the filename here
file_again = input("> ")

# Open the corresponding text file
txt_again = open(file_again)

# Print out the content of the text file
print(txt_again.read())
