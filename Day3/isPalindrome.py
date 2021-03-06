#! usr/bin/env python
import sys

def reverse(string):
    return string[::-1]

def isPalindrome(string):
    string = string.lower()
    return string == reverse(string)

def main():
    print ('''

    :palindrome: aba == aba, 7102017 == 7102017
    A string is said to be palindrome if reverse 
    of the string is same as string. 
    For example, "radar" is palindrome, but "radix" is not palindrome.

    ''')
    while True:
        if sys.version_info[0] == 2:
            input = raw_input

        print("type any string")
        string = str(input('>> '))
        palindrome = isPalindrome(string)
        if palindrome:
            print ("Yay, {} is a palindrome".format(string))
            break
        else:
            print("Aww! {} is not a palindrome".format(string))
            print("try another? y or n")
            answer = str(input(">> "))
            if answer.lower() in ['yes', 'y', 'yh', 'yes']:
                continue
            else:
                print("Have a great day!")
                break

if __name__ == '__main__':
    main()