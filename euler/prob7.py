__author__ = 'andythomas'
import datetime
import math

def checkPrime (primes, candidate):
    isPrime = True

    toCheck = math.ceil(math.sqrt(candidate))
    for p in primes:
        res = toCheck % p
#        print ("candidate = %d prime = %d res = %d" % (candidate, p, res))
        if res == 0:
            isPrime = False
            break

    return isPrime

primes = [2,3,5,7]

start =  datetime.datetime.utcnow()

top = primes[-1]
#print top

#candidate = top + 2
#print candidate

while (len(primes) < 10001):
    top = primes[-1]
    candidate = top + 2

    found = False
    while found == False:
        found = checkPrime (primes, candidate)
        if found == False:
            candidate += 2

#   add the new prime number into the list.
    primes.append(candidate)
    
#    print primes
#    print

print primes

end =  datetime.datetime.utcnow()

print ("started at %s" % (start))
answer = primes[-1]
print ("The answer = %d" % (answer))

print ("ended at %s" % (end))
