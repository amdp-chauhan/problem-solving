# Geomatric Sum using Recursion

def findGeometricSum(k):
    if k==0:
        return 1

    sum = findGeometricSum(k-1) + (1/2**k)

    return sum

n=int(input())
print('%.5f' % findGeometricSum(n))
