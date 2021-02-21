def greet_name():
    valid_name = "Jannah"
    name_entered = input("who are you?\n")

    while name_entered != valid_name:
        name_entered = input("unknown person:\n")

    print("SUCCESS - :-) " + valid_name)


# TODO - i MUST REMEMBER TO CALL THE FUNCTION :-(
greet_name()

