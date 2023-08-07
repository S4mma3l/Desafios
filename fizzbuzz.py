#!/usr/bin/env python3


# fizz buzz
def fizzbuzz():
    for indice in range(1, 101):
        if indice % 3 == 0 and indice % 5 == 0:
            print("fizzbuzz")
        elif indice % 3 == 0:
            print("fizz")
        elif indice % 5 == 0:
            print("buzz")
        else:
            print(indice)


fizzbuzz()
