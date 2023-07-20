#!/usr/bin/python3
import random 
number = random.randint(-10000, 10000)
numbersa = str(number)
last_digit_unsigned = int(numbersa[-1])
karshe = -last_digit_unsigned
if number < 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, karshe)) 
elif last_digit_unsigned > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,  last_digit_unsigned))
elif last_digit_unsigned == 0:
     print("Last digit of {} is {} and is 0".format(number, last_digit_unsigned))
elif last_digit_unsigned < 6 and last_digit_unsigned >= 1:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,  last_digit_unsigned))

