# using recursion to implement a countdown timer

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)
        # if I were to have a print after this would get "unwound" and called 5 times to print
        print("foo")


# testing!
countdown(5)