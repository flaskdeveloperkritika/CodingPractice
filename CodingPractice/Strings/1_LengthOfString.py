string1 = 'Hello Kritika'

# way 1
print(len(string1))

# way 2
for i in string1:
    if len(string1) == 0:
        print('0')
print(len(string1))

# way 3
counter = 0
for char in string1:
    counter = counter + 1
print('length of the string1 is: ', counter)


# way 4
def length(str1):
    counter = 0
    for char in string1:
        counter = counter + 1
    print('length of the string1 is: ', counter)


length(string1)


# way 5
class LengthOfString:
    def __init__(self, str1):
        self.str1 = str1

    def length(self):
        counter = 0
        for char in string1:
            counter = counter + 1
        print('length of the string1 is: ', counter)


length = LengthOfString(string1)
length.length()
