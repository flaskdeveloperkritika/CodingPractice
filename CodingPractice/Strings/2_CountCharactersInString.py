string1 = 'Hello Kritika'

# way 1
print(string1.count('a'))

# way 2
count = 0
"""for chars in string1:
    if 'a' in chars:
        count = count + 1
        print('l occurs ', count, 'times!!')"""

for chars in string1:
    if chars == 'l':
        count = count + 1
print('l occurs ', count, 'times')

# way 3
count = 0
string_input = input('Enter String : ')
char_count = input('Enter character whose count you want to find : ')

for chars in string_input:
    if chars == char_count:
        count = count + 1
print(char_count, ' occurs ', count, ' times.')

# way 4


def count_chracters():
    count = 0
    string_input = input('Enter String : ')
    char_count = input('Enter character whose count you want to find : ')

    for chars in string_input:
        if chars == char_count:
            count = count + 1
    print(char_count, ' occurs ', count, ' times.')


count_chracters()


# way 5
def count_chracters(string_input, char_count):
    count = 0
    '''string_input = input('Enter String : ')
    char_count = input('Enter character whose count you want to find : ')'''

    for chars in string_input:
        if chars == char_count:
            count = count + 1
    print(char_count, ' occurs ', count, ' times.')


count_chracters('Hey Kritika', 'i')


# way 6


class CountCharsString:
    def __init__(self):
        self.count = 0

    def count_chracters(self):
        string_input = input('Enter String : ')
        char_count = input('Enter character whose count you want to find : ')

        for chars in string_input:
            if chars == char_count:
                self.count = self.count + 1
        print(char_count, ' occurs ', self.count, ' times.')


countcharsstring = CountCharsString()
countcharsstring.count_chracters()


class CountCharsString:
    def __init__(self, string_input, char_count):
        self.count = 0
        self.string_input = string_input
        self.char_count = char_count

    def count_chracters(self):
        '''
        string_input = input('Enter String : ')
        char_count = input('Enter character whose count you want to find : ')'''

        for chars in self.string_input:
            if chars == self.char_count:
                self.count = self.count + 1
        print(self.char_count, ' occurs ', self.count, ' times.')


countcharsstring1 = CountCharsString('Kritika Trivedi', 'i')
countcharsstring2 = CountCharsString('Kritika Trivedi', 'T')  # case sensitive
countcharsstring3 = CountCharsString('Kritika Trivedi', 't')  # case sensitive
countcharsstring1.count_chracters()
countcharsstring2.count_chracters()
countcharsstring3.count_chracters()

