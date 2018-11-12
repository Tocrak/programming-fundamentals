import sys

def count_vowels(string):
    vowels = 'aeiou'
    vowel_nr = 0
    for letter in string:
        if letter.lower() in vowels:
            vowel_nr += 1
    return vowel_nr

string = sys.argv[1]
print('{0} contains {1} vowels'.format(string, count_vowels(string)))