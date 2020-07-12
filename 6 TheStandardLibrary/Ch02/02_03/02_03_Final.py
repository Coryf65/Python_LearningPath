# Random Module
import random

# this helps to choose random numbers 

# Random Numbers
print('Get a random number:', random.random())

print('\nFlipping a coin...')
decider = random.randrange(2)
if decider == 0:
    print("HEADS")
else:
    print("TAILS")
print('decider value =', decider)

# prints a random number 1 -> 6
print('\nRolling a six sided die...')
print("You rolled a " + str(random.randrange(1, 7)))

# Random Choices
lotteryWinners = random.sample(range(100), 5) # 0 -> 99 and choosing 5 numbers
print('\nRandomly choosing a lottery winner!')
print('picking number: 0 Thru 99 and choosing 5 numbers')
print('Winning Numbers!', lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print('\nPicking a Random Pet from a list:', random.choice(possiblePets))

cards = ["Jack", "Queen", "King", "Ace"]
print('\nShuffling Cards')
random.shuffle(cards)
print('Our Cards:', cards)