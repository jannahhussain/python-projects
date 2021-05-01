"""

    1) Encapsulation - what is it?

    It is when the member variables are private and data is only available through get methods

    This is by design because we are not allowed to directly change the state

"""


class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname
        self._dob = None
        self._height = None
        self._weight = None
        self._gender = None
        self._address = None

    def set_first_name(self, fname):
        self._first_name = fname

    def set_lastname_name(self, lname):
        self._last_name = lname

    def set_dob(self, dob):
        self._dob = dob

    def set_height(self, height):
        self._height = height

    def set_weight(self, weight):
        self._weight = weight

    def set_gender(self, gender):
        self._gender = gender

    def set_address(self, address):
        self._address = address

    """ getters """
    def get_first_name(self):
        return self._first_name

    def get_lastname_name(self):
        return self._last_name

    def get_dob(self):
        return self._dob

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_gender(self):
        return self._gender

    def get_address(self):
        return self._address

    def get_age(self):
        '''
        we only need get age as we have to derive it
        :return: 
        '''
        pass



