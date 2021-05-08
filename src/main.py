

from src.oop.person import Person

person1 = Person("Jannah", "Hussain")
person2 = Person("Rumaisah", "Hussain")
person3 = Person("Aboodi", "Hussain")
person4 = Person("Dad", "Hussain")

""" here we are setting the 'dob' state for each person object """
person1.set_dob("2007-08-22")
person2.set_dob("2011-03-14")
person3.set_dob("2014-04-27")
person4.set_dob("1973-01-04")

people_list = [person1, person2, person3, person4]

""" here we are applying the behaviours of the person objects """
for person in people_list:
    print(person.get_first_name())
    print(person.get_lastname_name())
    print(person.get_age())
    print("--------------")






