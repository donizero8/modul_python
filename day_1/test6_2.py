number = 5

def summation(first, second):
    total = first + second + number
    return total

outer_total = summation(10, 20)

print("The first number we initialised was " + str(number))
print("The total after summation is " + str(outer_total))
