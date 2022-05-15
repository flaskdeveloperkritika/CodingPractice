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
