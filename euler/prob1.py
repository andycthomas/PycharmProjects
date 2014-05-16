__author__ = 'andythomas'


#Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
for x in range(1,1000):
    y = x % 3
    # check for multiples of 3.
    if (y == 0):
        total += x
    else:
        # check for multiple of 5, but make sure we dont take multiples of 15.
        y = x % 5
        if (y == 0):
            total += x

print ("the total is %d" % total)
