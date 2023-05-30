# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split(

##"a a a b c a a d c d d"
data_ = [i for i in input("Введите символы: ").split()]
print(data_)
data_2=set(data_)

for i in data_2:
    count=0
    for j in range(len(data_)):
      if i==data_[j]:
        #  print (f"{data_[j]}_{count}")
         if count>0: data_[j]=f"{data_[j]}_{count}"
         count+=1
print(*data_)

input_str = "a a a b c a a d c d d".split()
letters = {}
for i in input_str:
    if i in letters.keys():
        print(i + "_" + str(letters[i]), end=" ")
        letters[i] += 1
    else:
        print(i, end=" ")
        letters[i] = 1