# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def find_indices_in_range(lst, min_val, max_val):
    indices = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indices.append(i)
    return indices

input_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

result = find_indices_in_range(input_list, min_value, max_value)
print(result)
