# Getting more control over formatting
from datetime import datetime

now = datetime.now()

# Ways of abbreviating the date and time
# similiar to String Formatting
print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%A %B %d"))

print(now.strftime("%H : %M : %S %p"))

print(now.strftime("%y %Y"))