import sys

print('''
        Count Vowels - Enter a string and the program counts the number of vowels in the text. 
        For added complexity have it report the number of each vowel found in a long text.

    ''')

def count_vowel(string):
    vowel = 'aeiou'
    vowel_dict = {char:string.lower().count(char) for char in vowel}

    print ("number of vowel in {} is {}".format(string, sum(vowel_dict.values())))
    print (vowel_dict)


if __name__ == '__main__':

    if sys.version_info[0] == 2:
        input = raw_input

    print ('Type a string')
    input_string = str(input(">> "))
    count_vowel(input_string)
