""" Loading the Dishwasher """

# dirty dishes in the sink
sink = ['bowl','plate','cup']

# This will run until the sink is empty
for dish in sink:
    print('Putting {} in the dishwasher'.format(dish))
    # if you remove items inside a loop that you are looping through
    # the index changes and messes up the index
    sink.remove(dish)

# now the plate is still left due to changing the index
print(sink)