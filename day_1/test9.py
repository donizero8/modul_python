def addition(*args):
    total = 0
    for i in args:
        total += i
    return total

answer = addition(20, 10, 5, 1)
print(answer)
