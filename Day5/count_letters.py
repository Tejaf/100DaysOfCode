'''
    Count Letters in a Speech - Attached is a text file containing the farewell speech of Barack Obama. 
    The function should read content from the file, count and record all letters of the alphabet present. 
    Output should be like => a: 20, b: 10, ...z: 5. 
    It should also be case insensitive i.e 'a' == 'A'.
'''

import string
def count_letters(filename):
    alphabeths = string.ascii_lowercase
    with open(filename) as f:
        file_content =  f.read().lower()
        letter_count = {letter:file_content.count(letter) for letter in alphabeths}
        print letter_count


if __name__ == '__main__':
    count_letters("obama_speech.txt")