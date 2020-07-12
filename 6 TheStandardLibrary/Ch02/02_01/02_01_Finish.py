# Math Module Part I

# this module is a 'builtin', you don't need to download from the web
import math

# Constants
print('pi =', math.pi)
print('constant e: ', math.e)

print('constant Not A Numer: ', math.nan)
print('constant infininity: ', math.inf)
print('constant Negative infininity: ',-math.inf)

# Trigonometry
obst_direction = math.cos(math.pi / 4) # 45 degree angle cosine value
print(obst_direction)
print(math.sin(math.pi / 4)) # checking if the sine is the same value, 45

# Ceiling and Floor
cookies = 10.3
candy = 7
print(f'math.ceil({10.3}):', math.ceil(cookies))
print(f'math.ceil({7}):', math.ceil(candy))

age = 47.9
otherAge = 47
# what  is your age? 47 not 47.9
print(f'math.floor({47.9}):', math.floor(age))
print(f'math.floor({47}):',math.floor(otherAge))