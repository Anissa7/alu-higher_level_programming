#!/usr/bin/python3
import random
number = random.radint(-10000, 10000)
last = abs(abs(number)%10)
if number > 0:
    digit = number %10
else:
    digit =((number * -1) % 10) * -1

    print("last digit of {:d} is{:8} .format(number,digit), end="")
if digit  == 0:
    print( "and is 0")
elif number < or digit < 6:
    print
    ("and is less than 6 and not 0")
else:
    print ( "and is greater than 5")
