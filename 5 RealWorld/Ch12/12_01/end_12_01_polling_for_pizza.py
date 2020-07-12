""" Polling for Pizza to Cure My Hunger """

# polling will consantly wait for the event to occur

# when running a while loop to use a polling routine add a wait to prevent very high system usage

import time

hungry = True # I need a pizza!

print(dir())

while(hungry):

    print('Opening the front door')
    front_door = open('c:/Users/Cory/Documents/_Code/Python_LearningPath/5 RealWorld/Ch12/12_01/front_door.txt', 'r')

    if "Pizza Guy" in front_door:
        print("Pizza's here!")
        hungry = False
    else:
        print("Not yet...")

    print('Closing the front door.')
    front_door.close()

    time.sleep(1) # rest for 1 second
