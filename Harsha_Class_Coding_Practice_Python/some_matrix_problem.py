n = [[10,20,30],[40,50,60],[70,80,90]]
for string in n:
    for str1 in string:
        print(str1, end=' ')
    print()

import copy

li1 = [1, 2, [3, 5], 4]

li2 = copy.copy(li1)

li3 = copy.deepcopy(li1)

print(li1)
print(li2)
print(li3)

li2.append(2)
li3.append(3)
print(li1, li2, li3)
