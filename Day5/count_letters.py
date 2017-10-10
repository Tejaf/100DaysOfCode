'''
    Count Letters in a Speech* - Attached is a text file containing the farewell speech of Barack Obama. 
    The function should read content from the file, count and record all letters of the alphabet present. 
    Output should be like => a: 20, b: 10, ...z: 5. 
    It should also be case insensitive i.e 'a' == 'A'.
'''

import string
def count_letters(filename):
    alphabeth = string.ascii_lowercase
    with open(filename) as f:
        speech =  f.read().lower()
        letter_count = {letter:speech.count(letter) for letter in alphabeth}
        print letter_count


count_letters("obama_speech.txt")