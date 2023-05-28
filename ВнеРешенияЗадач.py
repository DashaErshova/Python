# data = [int(i) for i in input("Введите числа: ").split()]
# print(data)

# list_1 = [1, -1.575, 'Hello, world!', True]
# list
# array(import array || import numpy)
# t = (1, 2)
# t[0] += 1
# tuple 
# dict
# set
set_1 = {1, 2, 3, 4}
set_1.add(56)
print(*set_1)


# data = [[1, -1.575], ['Hello, world', True], [15, -7]]
# #           0                  1                 2
# print(data[2][0])

data = {"Ivan": 27, 'Alexandr': 36, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'fotball']}}
# key: value
print(data['Konstantin']['hobby'][0])
# .values()
# .keys()
print(list(data.values()))
print(list(data.keys()))