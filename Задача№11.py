# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Введите число: "))
a0 = 0
a1 = 1
a2 = 0
i = 2
while a2 < n:
    a2 = a1 + a0 # Для того чтобы найти 3-ое число, мы складываем 1-ое и 2-ое
    a0 = a1 # Для того чтобы найти 4-ое число, мы складываем 2-ое и 3-е
    a1 = a2
    i += 1
    if a2 > n:
        i = -1
if i == -1:
    print(i)
else:
    print(i)