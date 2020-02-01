def add_number(num):
    def adder(number):
        'adder is a closure'
        return num + number
    return adder

a_10 = add_number(10)
print(a_10(21))
