# Sorted(x)
# param iterable: Iterable[_T]

# Return a new list containing all items from the iterable in ascending order.
# A custom key function can be supplied to customize the sort order, and the
# reverse flag can be set to request the result in descending order.

# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters, converts all to uppercase, case insensitive
print(sorted("My favorite child is Linda".split(), key=str.upper))
# reverses the order
print(sorted(pointsInaGame, reverse=True))

leaderBoard = {231: "CKL", 123:"ABC", 432:"JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

# you can also sort Dict() !
students = [ ('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student:student[0]))
print(sorted(students, key=lambda student:student[1]))
print(sorted(students, key=lambda student:student[2]))

