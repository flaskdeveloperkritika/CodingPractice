dict_dup = {1: 'hi', 2: 'bye', 3: 'raj', 2: 'hey', 2: 'hello', 3: 'ahe'}

count_dupKey = {}
for key, value in dict_dup.items():
    print(list(dict_dup.keys())[list(dict_dup.values()).index(value)])


'''
for key in dict_dup:
    if key in count_dupKey:
        count_dupKey[key] += 1
        # count_dupKey[key] = lambda x: x[1]
        # print(count_dupKey)
    else:
        count_dupKey[key] = 1

print(count_dupKey)
''''''
# list out keys and values separately
key_list = list(dict_dup.keys())
val_list = list(dict_dup.values())

# print key with val 100
position = val_list.index('hi')
print(key_list[position])

# print key with val 112
# position = val_list.index('raj')
# print(key_list[position])

# one-liner
# print(list(dict_dup.keys())[list(dict_dup.values()).index('raj')])


mydict = {'george': 16, 'amber': 19, 'george': 18}  # 'honey': 18
print(list(mydict.keys())[list(mydict.values()).index(18)])'''

