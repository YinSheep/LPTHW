# define a function that takes two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print out a string with a parameter
    print(f"You have {cheese_count} cheeses!")
    # print out a string with a parameter
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print out a string with no parameter
    print("Man that's enough for a party!")
    # print out a string with no parameter
    print("Get a blanket. \n")

# print out a string
print("We can just give the function numbers directly:")
# run the function with 2 parameters
cheese_and_crackers(20,30)

# print out a string
print("OR, we can use variables from our script:")
# make two variables
amount_of_cheese = 10
amount_of_crackers = 50

# run the function with 2 variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# run the function with the sum of two integers
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# run the function with the sum of a number and a paramter
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
