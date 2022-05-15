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