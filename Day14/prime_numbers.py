#! usr/env python2.7

'''
    prime numbers are numbers that can only be divided by one and itself
'''

def prime(n):
    for i in range(n):
        isPrime = True
        for j in range(2, n+1):
            if i%j == 0 and j != i:
                isPrime = False

        if isPrime:
            print i,

prime(100) # 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
