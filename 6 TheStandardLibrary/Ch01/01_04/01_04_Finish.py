# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

# inclusive 0-29, 30 numbers
numberedContestants = range(30)

# converts into a tuple
print(list(numberedContestants))

for c in list(numberedContestants):
    print(f"Contestant {str(c)} is here")

# Starting Point, End Point, count by
luckyWinners = range(7, 30, 5)

# display winners
print(list(luckyWinners))