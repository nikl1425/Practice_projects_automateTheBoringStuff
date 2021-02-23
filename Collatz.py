import sys, time


def collatz(number):
    try:
        number = int(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
    except ValueError:
        print("this isnt a number")

value = input("please enter a value: \n")
collatz(value)


