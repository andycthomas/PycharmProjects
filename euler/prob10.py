__author__ = 'andythomas'

#pythagoran triples

def check (nums):
#    print nums

    a = nums[0]
    b = nums[1]
    c = nums[2]

    lhs = (a*a) + (b*b)
    rhs = c*c

    if (lhs == rhs):
        return True
    else:
        return False

k = [200, 375, 425]
print k
print k[0] + k[1] + k[2]
print k[0] * k[1] * k[2]
exit (0)

for i in range (1,1000,1):
#    print i

    for j in range (1,1000,1):
#        print i, j
        
        for k in range (1,1000,1):
#            print i, j, k
            sum = i + j + k

            if ( sum == 1000):
#                print i,j,k

                nums = [i,j,k]
                nums.sort()

                if (check(nums) == True):
                    print nums