from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, place, say):
        Animal.__init__(self, name, age)
        self.place = place
        self.say = say

    def display_info(self):
        Animal.display_info(self)
        print(self.name, ' live in ', self.place)

    def display_say(self):
        print(self.name, ' say ', self.say)
