__author__ = 'andythomas'

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

next = 0
prev = 1
curr = 2

total = 2

while next < 4000000:
    next = prev + curr
    print ("prev = %d curr = %d next = %d" % (prev, curr, next))
    prev = curr
    curr = next

    if (next % 2 == 0):
        total += next
        
print ("total = %d" % (total))

