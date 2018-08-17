# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe()” method (which prints “name” and “kind” in a sentence).
class Food:
    name = 'Orange'
    kind = 'citrus'

    def __init__(self):
        # self.id = str(uuid4())
        self.first_name = 'Gabriel'
        self.last_name = 'Chivoiu'

    def __repr__(self):
        return str(self.__dict__)

    def describe(self):
        print('{} is part of the {} family'.format(self.name, self.kind))



# 2) Try turning describe() from an instance method into a class and a static method. Change it back to an instance method thereafter.
    
    @classmethod
    def describe_1(cls):
        print('{} is part of the {} family'.format(cls.name, cls.kind))

    @staticmethod
    def describe_2(name = 'Apple', kind = 'Rosaceae'):
        print('{} is part of the {} family'.format(name, kind))

inst = Food()
inst.describe()

Food.describe_1()

Food.describe_2()

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook()” method to “Meat” and “clean()” to “Fruit”.

class Meat(Food):
    def cook(self):
        print('cooking')

class Fruit(Food):
    def clean(self):
        print('cleaning')

# 4) Overwrite a “dunder” method to be able to print your “Food” class.

food1 = Food()
print(food1)