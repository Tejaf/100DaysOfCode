#!usr/bin/env python2.7

import string
import random
import re

def generate_password():
    try:
        while True:
            password_len = int(raw_input("Type the length of the password you want to generate. This shouldn't be less than 6: "))
            if password_len > 6:
                char = re.sub(r'[:\`\'\"\(\),\./;<=>\?@\^\[\\\]{|}~\t\n\r\x0b\x0c]', '', string.printable)
                hash_password = ''

                for i in range(password_len):
                    hash_password += char[int((random.random() * len(char) - 2 ) + 1)]

                return hash_password
            else:
                print('Your number must be greater than 6')
                continue
        
    except ValueError:
        return ('Invalid number.')

print (generate_password())