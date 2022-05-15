dict_blank = {'name': None, 'id': None}
dict_empty = {}
# dict_ls = {}
output_list = []
# o_l = []
num = int(input('how many values you want to enter?'))
for i in range(num):
    name = input('enter name:')
    id = input('enter id:')

    dict_blank['name'] = name
    dict_blank['id'] = id


    # o_l.append(dict_blank)


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