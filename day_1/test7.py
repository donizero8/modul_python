def summation(first, second):
    total = first + second
    return total

def main():
    outer_total = summation(10, 20) * 2
    print("Double the total is " + str(outer_total))

if __name__ == "__main__":
    main()
