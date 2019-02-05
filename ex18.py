# this one is like your scripts with argv
# this function takes two input paramters and print them out
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# this function also takes two input paramters and print them out
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# takes one parameter and print it out
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
# this is an empty function
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
