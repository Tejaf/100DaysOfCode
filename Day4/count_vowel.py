print('''
        Count Vowels - Enter a string and the program counts the number of vowels in the text. 
        For added complexity have it report the number of each vowel found in a long text.

    ''')

def count_vowel(string):
    vowel = 'aeiou'
    vowel_count = map(string.count, vowel)
    vowel_dict = {}
    for i, char in enumerate(vowel):
        vowel_dict[char] = vowel_count[i]

    for k,v in vowel_dict.items():
        if v == 0:
            del vowel_dict[k]

    print "number of vowel in {} is {}".format(string, sum(vowel_dict.values()))
    print vowel_dict


if __name__ == '__main__':
    print 'Type a string'
    input_string = raw_input(">> ")
    count_vowel(input_string)
