class Person:
    def __init__(self, name, age, height_in_cm):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm
    def __str__(self):
        return "Hello my name {} and I {} years old.".format(self.name, self.age)

person1 = Person("Cubert", 62, 180)
print(person1)
