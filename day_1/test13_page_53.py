class Person:
    def __init__(self, name, age, height_in_cm):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm
    def greet(self, person):
        print("Hi {}".format(person.name))
    def __str__(self):
        return "Hello my name {} and I {} years old.".format(self.name, self.age)

joe = Person("Josef", 31, 174)
gabby = Person("Gabriela", 32, 169)
joe.greet(gabby)
