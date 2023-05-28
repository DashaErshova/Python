# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет: "))
coins = []
for i in range(n):
    coins.append(int(input("Орел(1) или решка(0)? ")))

quantity_orlov = 0
quantity_reshek = 0

for coin in coins:
    if coin == 0:
        quantity_orlov += 1
    if coin == 1:
        quantity_reshek += 1

if quantity_orlov > quantity_reshek:
    print(f"Переверните {quantity_reshek} монет с решки на орла, их меньше всего")
else:
    print(f"Переверните {quantity_orlov} монет с орла на решку, их меньше всего")
