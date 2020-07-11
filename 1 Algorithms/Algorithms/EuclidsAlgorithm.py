# A greatest Common Denominator (Euclid's Algorithm)

def GreatestCommonDenominator(a, b):
    while(b != 0):
        # storing a
        temp = a
        a = b
        # getting the remainder
        b = temp % b

    return a

# testing out our new function
print(GreatestCommonDenominator(60, 96)) # should be 12
print(GreatestCommonDenominator(20, 8))  # should be 4