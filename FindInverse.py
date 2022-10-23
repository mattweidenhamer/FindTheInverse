from math import gcd

def FindInverse(number, mod):
    if gcd(number, mod) != mod:
        return None

def shrink_number(numberToEqual, numberToMultiply): 
    multiplyingNumber = 0
    # Repeat until multiplyingnumber times number2 is greater than number1
    while(numberToMultiply * multiplyingNumber < numberToEqual):
        multiplyingNumber = multiplyingNumber + 1
    remainder = numberToEqual - (multiplyingNumber * numberToMultiply)