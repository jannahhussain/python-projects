def run():

    """
     D I C T I O N A R Y   S T U F F

     name: L Hussain
     date: 17-Apr-2021

     Go to: https://www.w3schools.com/python/python_dictionaries.asp

    """

    ''' here I am creating and empty dictionary'''
    fruit_dictionary = {}
    print(fruit_dictionary)

    ''' here i am adding new key/value pair(s) to the dictionary'''
    fruit_dictionary["oranges"] = 20
    fruit_dictionary["pears"] = 5

    print(fruit_dictionary)

    ''' here i am updating orages in the dictionary'''
    fruit_dictionary["oranges"] = 30
    print(fruit_dictionary)

    ''' here i am deleting 'pears' from the dictionary'''
    del fruit_dictionary["pears"]
    print(fruit_dictionary)

    ''' here i am performing a lookup against my dictionary to get how many oranges'''
    print(fruit_dictionary["oranges"])


run()
