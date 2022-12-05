# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

list = [1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 10, 5]
list2 = []
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            list2.append(list[i])

list = set(list)
list2 = set(list2)

difference = tuple(list.difference(list2))
print(difference)

