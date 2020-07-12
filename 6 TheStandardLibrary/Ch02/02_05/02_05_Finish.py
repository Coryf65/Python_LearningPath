# Itertools
import itertools

# Infinite Counting loop, stops when we hit 80, 50 to 80 counting down by 5s
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break


# Infinite Cycling, prints Racecar 50 times
x = 0
for c in itertools.cycle("RACECAR"):
    print(c)
    x = x + 1
    if x > 50:
        break

# Infinite Repeating, repeat True 100 times over
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x > 100:
        break