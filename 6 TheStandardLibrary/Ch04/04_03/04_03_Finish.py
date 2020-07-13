# Calendar Module

# delta time testing
from datetime import datetime, timedelta
import calendar

now = datetime.now()

# test date is now the date, two days from now
testDate = now + timedelta(days=2)

# date 3 weeks ago
myFirstLinkedInCourse = now - timedelta(weeks=3)

print('2 days from now', testDate.date())
print('3 weeks ago', myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
    print("Comparison works\n")

# October from 2001
cal = calendar.month(2001, 10)
print(cal)

cal2 = calendar.weekday(2001, 10, 11)
print(f'10-11-2001 is the {cal2} day of the week')

print('is 1999 a leap year?', calendar.isleap(1999))

print('is 2000 a leap year?',calendar.isleap(2000))