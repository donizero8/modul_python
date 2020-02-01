class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed
    def vocalize(self):
        print("Meow")
    def print_facts(self):
        print("The {} ".format(type(self).__name__.lower()), end="")
        print("weighs {}kg,".format(self.mass_in_kg), end="")
        print(" has a lifespan of {} years and ".format(self.lifespan_in_years), end="")
        print("can run at a maximum speed of {}kph.".format(self.speed_in_kph))

class Cheetah(Cat):
    # Update this code
    def __init__(self, mass, lifespan, speed):
        super().__init__(mass, lifespan, speed)
        self.spotted_coat = True
    def vocalize(self):
        print("Chirrup")
        
class Lion(Cat):
    def vocalize(self):
        print("ROAR")

cheetah = Cheetah(72, 12, 120)
cheetah.print_facts()

print("=" * 10)
print("Cheetah Vocal :")
cheetah.vocalize()
print("=" * 10)
print("is cheetah spotted? ", cheetah.spotted_coat)
