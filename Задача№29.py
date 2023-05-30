# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.


N = []
while True:
    num = int(input("Введите число (для завершения введите 0): "))
    if num == 0:
        break
    N.append(num)

if len(N) == 0:
    print("Последовательность пуста.")
else:
    max_element = max(N)
    print("Наибольший элемент последовательности, завершающейся первым встретившимся нулем:", max_element)
