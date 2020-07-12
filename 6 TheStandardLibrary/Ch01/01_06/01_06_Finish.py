# Python Rounding, Absolute Value, and Exponents

# round()
# Rounds up or down and returns an int
myGPA = 3.6
print(f'GPA: {myGPA} rounded:', round(myGPA))
amountOfSalt = 1.4
print(f'Amount of Salt: {amountOfSalt} rounded:', round(amountOfSalt))

apple = -1.2
print(round(apple))
google = -1.6
print(round(google))

# abs()
# Absolute Value, takes a whole number or decimal, outputs number representing the ABS of the input
distanceAway = -13
print(f'distanceAway: {distanceAway} abs(distanceAway):', abs(distanceAway))
lengthOfRootInGround = -2.5
print(f'How deep are the roots? {lengthOfRootInGround} ABS(lengthOfRootInGround):', abs(lengthOfRootInGround))

# pow(x, y)
# input x=Base, y=Exponent output the representation
chanceOfTails = 0.5 # chance of flipping a coin to tails
inARowTails = 3 # chance of rolling 3 in a row
print('Chance of flipping a coin to tails 3 times in a row:', pow(chanceOfTails, inARowTails))

chanceOfOne = .167
inARowOne = 2
print(pow(chanceOfOne, inARowOne))