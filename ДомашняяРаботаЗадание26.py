# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))


def power(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * power(number, exponent - 1)
result = power(A, B)
print(f"{A} в степени {B} = {result}")