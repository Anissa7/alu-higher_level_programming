#!/usr/bin/python3
import random
number = random.radint(-10000, 10000)
last = abs(abs(number)%10)
if number < 0:
    last = -1 * last
if last >5:
    print("last digit of" ,number, "is", last, "and is greater than 5")
elif last == 0:
    print("last digit of " , number "is", last "and is 0")
eli last < 6:
    print ("last digit of " , number, "is", last, "and is less than 6 and not 0")
    
