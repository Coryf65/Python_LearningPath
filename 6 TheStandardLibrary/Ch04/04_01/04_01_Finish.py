# Datetime Module Part I
from datetime import datetime

# we can get lots of details about the time
now = datetime.now()

print('Current Date:', now.date())

print('Current Year:', now.year)

print('Current Month:', now.month)

print('Current Hour:', now.hour)

print('Current Minutes:', now.minute)

print('Current Seconds:', now.second)

print('Current Time:', now.time()) # a method that combines many properties