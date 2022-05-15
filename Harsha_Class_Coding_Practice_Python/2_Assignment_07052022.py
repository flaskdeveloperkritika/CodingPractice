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
