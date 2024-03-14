#!/usr/bin/python3
def fizzbuzz():
    for w in range(1, 101):
        if w % 3 == 0:
            print("{}".format('Fizz'), end=" ")
        elif w % 5 == 0:
            print("{}".format('Buzz'), end=" ")
        elif w % 3 == 0 and w % 5 == 0:
            print("{}".format("FizzBuzz"), end = " ")
        else:
            print(w, end=" ")
