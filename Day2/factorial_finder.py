import sys

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print('''
        Hello,
        this is a factorial finder script  
        fact(n) = n! = n * (n-1) * (n-2) * ... * 1
        e.g fact(4) = 4*3*2*1 = 24
    ''')

while True:
    if sys.version_info[0] == 2:
        input = raw_input

    print('Type a positive number')
    number = int(input('>> '))
    answer = factorial(number)
    print('The factorial of {} is {}'.format(number, answer))
    print ("try again? y or n ")
    reply = str(input('>> '))
    if reply.lower() in ['yes', 'y', 'yeah', 'yup']:
        continue
    else:
        print("Now you know factorial. Good job!")
        break


# using generators
def fact_using_generator(number):
    count = 1
    fact = 1
    while count <= number:
        yield fact
        count += 1
        fact = fact * count

