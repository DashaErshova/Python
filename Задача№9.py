# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

n = int(input("Введите число: "))
i = 2
result = 1
while i <= n:
    result *= i # result = result * i
    i += 1
print(f'{n}! = {result}')




# n = int(input("Введите число: "))
# result = 1
# m = n
# while n > 1:
#     result *= n # result = result * i
#     n -= 1
# print(f'{m}! = {result}')