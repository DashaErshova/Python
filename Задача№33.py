# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def vasia(array):
   min_numbers = min(array)
   max_numbers = max(array)
   for i in range(len(array)):
      if array[i] == max_numbers:
         array[i] = min_numbers
   return array

n = int(input())
list_1 = [int(i) for i in input().split()][:n]
print(*vasia(list_1))