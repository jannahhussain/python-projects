def name_greet():
    name_greet = "Jannah"
    name_entered = input("what is your name?")

    while name_entered != name_greet:
        name_entered = input("that is incorrect, please try again.")

    print("hello " + name_greet())

# Using logical operators return true for this function using an if statement
# def logical_operator():
#     a = True
#     b = False
#     c = True
#     if a is True or b is False:
#         return True
#     if c is True and a is True:
#         return True
#
# print(logical_operator())
