list_of_strings = ['hi', 'hey', 'hello', 'how are you doing?', 'I am doing great, thank you for asking.']

'''longest_string = len(max(list_of_strings))
print(longest_string)'''
# way 1
max_len = -1
for string in list_of_strings:
    if len(string) > max_len:
        max_len = len(string)
        result = string

print(result, ' is the longest string having maximum length of ', len(string))
'''if len(list_of_strings[i]) > len(list_of_strings[i+1]):
        print('length of ', list_of_strings[i], ' is greatest')'''


def longest_string(list_of_strings):
    max_len = -1
    for string in list_of_strings:
        if len(string) > max_len:
            max_len = len(string)
            result = string

    print(result, ' is the longest string having maximum length of ', len(string))


longest_string(list_of_strings)


class LongestString:
    def __init__(self, list_of_strings):
        self.list_of_strings = list_of_strings

    def longest_string(self):
        max_len = -1
        for string in list_of_strings:
            if len(string) > max_len:
                max_len = len(string)
                result = string

        print(result, ' is the longest string having maximum length of ', len(string))


longest_string = LongestString(list_of_strings)
longest_string.longest_string()



