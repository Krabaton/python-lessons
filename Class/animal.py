class Animal:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Invalid data')

    @property
    def name(self):
        return self.__name

    # @staticmethod
    # @classmethod
    def display_info(self):
        print('It is ', self.__name, '\tAge: ', self.__age)

    def __str__(self):
        return 'Name: {} \t Age: {}'.format(self.__name, self.__age)
