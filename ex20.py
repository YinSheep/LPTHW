from sys import argv

script, input_file = argv

# a function that prints a file
def print_all(f):
    print(f.read())

# a function that returns to first byte of a file
def rewind(f):
    f.seek(0)

# a funcion that prints out certain line of a file
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# save the input file to a variable
current_file = open(input_file)

print("First let's print the whole file :\n")

# print out all the content of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewind the file
rewind(current_file)

print("Let's print three lines:")

# print each line of the file
current_line = 1
print_a_line(current_line, current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
