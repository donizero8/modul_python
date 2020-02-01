class Person:
    def __init__(self, name, age, height_in_cm):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm
    def greet(self, person):
        print("Hi {}".format(person.name))
    def birthday(self):
        self.age += 1
    def __str__(self):
        return "Hello my name {} and I {} years old.".format(self.name, self.age)

diana = Person("Diana", 28, 170)
print("Yesterday Diana {} year old".format(diana.age))
diana.birthday()
print("But today Diana {} year old".format(diana.age))
