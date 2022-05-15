string1 = 'hey kritika'

# using slicing

print(string1[0])
print(string1[1])
print(string1[-1])
print(string1[-2])

print(string1[-2:])

print(string1[:])
print(string1[::])
print(string1[0:])
print(string1[1:])
print(string1[0:2])
print(string1[0:5:2])
print(string1[0:5:3])
print(string1[:2:3])
print(string1[:4])
print(string1[:4:2])
print(string1[0:-1])
print(string1[-5:])
print(string1[4:-2])
print(string1[4:-2:3])

# using slice() constructor

print(string1[slice(-2,-12,2)])  # important
print(string1[slice(-2,-6,-2)])

