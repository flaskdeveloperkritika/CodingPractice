

print("Question 1: [1,2,3,4,[5,6,7,8]]")
print('using normal approach')
list1 = [1, 2, 3, 4, [5, 6, 7, 8]]

for i in list1[4]:
    print(i)

# list3 = [1, 2, 3, 4, [5, 6, 7, 8]]
print("Question 1: [1,2,3,4,[5,6,7,8]]")
print("using function-->")


def fun1(list1):
    for j in list1[4]:
        print(j)


fun1(list1)

print("Question 1: [1,2,3,4,[5,6,7,8]]")
print("using classes-->")


class List1:
    def __init__(self):
        self.list1 = [1, 2, 3, 4, [5, 6, 7, 8]]

    def fun2(self, list1):
        for i in list1[4]:
            print(i)


ls1 = List1()
ls1.fun2(list1)
print("Question 2: dict1 = {'a': 1, 'b': 2, 'c': {1: 1, 2: {'a': 1, 'b': 2, 'c': 'harsha'}}}")
print("using normal approach")
dict1 = {'a': 1, 'b': 2, 'c': {1: 1, 2: {'a': 1, 'b': 2, 'c': 'harsha'}}}


for i in dict1['c'][2]['c']:
    print(i)

str_replace = (dict1['c'][2]['c']).replace('a','k')
print(str_replace)

occurence_str = str_replace.count('k')
print(occurence_str)

print("Question 2: dict1 = {'a': 1, 'b': 2, 'c': {1: 1, 2: {'a': 1, 'b': 2, 'c': 'harsha'}}}")
print("using function-->")


def nested_dict(dict1):
    for i in dict1['c'][2]['c']:
        print(i)

    str_replace = (dict1['c'][2]['c']).replace('a', 'k')
    print(str_replace)

    occurence_str = str_replace.count('k')
    print(occurence_str)


nested_dict(dict1)

print("Question 2: dict1 = {'a': 1, 'b': 2, 'c': {1: 1, 2: {'a': 1, 'b': 2, 'c': 'harsha'}}}")
print("using classes -->")


class NestedDict():
    def __init__(self):
        self.dict1 = {'a': 1, 'b': 2, 'c': {1: 1, 2: {'a': 1, 'b': 2, 'c': 'harsha'}}}

    def nested_dict(self, dict1):
        for i in dict1['c'][2]['c']:
            print(i)

        str_replace = (dict1['c'][2]['c']).replace('a', 'k')
        print(str_replace)

        occurence_str = str_replace.count('k')
        print(occurence_str)


nested_dict = NestedDict()
nested_dict.nested_dict(dict1)


# 3 matrix = [[1,2,3], [4,5,6], [7,8,9]]
# o/p = transpose of matrix [[1,4,7], [2,5,8], [3,6,9]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for cols in range(len(matrix)):
        print(row[cols])
'''
transpose = []

# [[0,0][1,0][2,0], [0,1][1,1][2,1], [0,2][1,2][2,2]]
# for i in range(3):
# for j in i:
# print(matrix[i][j]

for i in matrix:
    for j in i:
        transpose.append(matrix[][])

for i in range(3):
    for j in range(3):
        transpose.append(matrix[i][j])
        print(transpose)
        # print(matrix[i][j])



for i in range(len(matrix)):
    for


'''

# 4 i/n --> ls1=[1,2,3] ls2=[4,5,6]
# o/p --> sum --> [5,7,9]
print('4th using normal approach!!')
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = []

for i in range(len(lst1)):
    for j in range(len(lst2)):
        if i == j:
            res = lst1[i] + lst2[j]
            lst3.append(res)
            break
print(lst3)

print('4th using function!!!')


def add_ele_lists(lst1, lst2):
    lst3 = []

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if i == j:
                res = lst1[i] + lst2[j]
                lst3.append(res)
                break
    print(lst3)


add_ele_lists(lst1, lst2)


print('4th using class!!!!')


class AddEleList():
    def __init__(self):
        self.lst1 = [1, 2, 3]
        self.lst2 = [4, 5, 6]

    def add_ele_lst(self, lst1, lst2):
        lst3 = []

        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if i == j:
                    res = lst1[i] + lst2[j]
                    lst3.append(res)
                    break
        print(lst3)


ad_ele_lst = AddEleList()
ad_ele_lst.add_ele_lst(lst1, lst2)


# 7 get all values  my_own = {'1': 'harsha', 'name': {'location': {'bgr': {'marath','white'},'che': {1: {'hyd','ra'}}}}}
# o/p --> ['harsha', 'marath', 'white', 'hyd', 'ra]
my_own = {'1': 'harsha', 'name': {'location': {'bgr': {'marath', 'white'}, 'che': {1: {'hyd', 'ra'}}}}}
for k1, v1 in my_own.items():
    print(v1)
    for k2, v2 in my_own['name'].items():
        print(v2)
    '''if v not in my_own.keys():
        print(v)'''

# mo['1'], for mo['name']['loc]['bgr'], for mo['che'][1]

"""for i in range(len(my_own)):
    for k1, v1 in my_own.items():
        print(v1)"""
print('--------------------------output-------------------------------------')
dict_dup = {1: 'hi', 2: 'bye', 3: 'raj', 2: 'hey', 2: 'hello', 3: 'ahe'}
output = {}
lst_key = []

for key in dict_dup:
    lst_key.append(key)

print(lst_key)

for ele in lst_key:
    if lst_key.count(ele) > 1:
        output.update({ele: lst_key.count(ele)})

'''for keys in dict_dup:
    if '''
print(output)


dict_blank = {'name': None, 'id': None}
dict_empty = {}
dict_ls = {}
output_list = []
o_l = []
num = int(input('how many values you want to enter?'))
for i in range(num):
    name = input('enter name:')
    id = input('enter id:')
    dict_blank['name'] = name
    dict_blank['id'] = id
    print(dict_blank)
    o_l.append(dict_blank)
    print(o_l)

    items1 = dict_empty.update({"name": name, "id": id})
    # print(items1)
    # print(dict_empty)
    output_list.append(dict_empty)

# print(items1)
print(dict_empty)

'''for key, val in dict_empty.items():
    output_list.append(dict_empty.items())
'''
# for key_another, val_another in items1.items():
#    dict_ls.update({key_another:val_another})
# print(dict_ls)
print(output_list)


