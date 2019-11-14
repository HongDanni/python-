#-*-coding:utf8-*-


class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        print('bmi')
        print(self.weight / (self.height**2))

    # @property
    def method(self):
        print("method")


per = Person("safly", 1.73, 75)
print(per.bmi)
print(Person.bmi)
print('*'*30)
print(per.method)
print(per.method())
print(Person.method)

