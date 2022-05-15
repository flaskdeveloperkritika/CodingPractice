def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v


a={4:1,6:2,7:{8:3,9:4,5:{10:5},2:6,6:{2:7,1:8}}}
print(list(NestedDictValues(a)))




'''emdict = {}
n = int(input('num'))
for i in range(n):
  k = input('key')
  v = input('val')
  emdict[k] = v

print(emdict)'''


def just_all_the_values(dict1):
    for value in dict1.values():
        if isinstance(value, dict):
            yield from just_all_the_values(value)
        else:
            yield value


my_own = {'1': 'harsha', 'name': {'location': {'bgr': {'marath', 'white'}, 'che': {1: {'hyd', 'ra'}}}}}
print(list(just_all_the_values(my_own)))


