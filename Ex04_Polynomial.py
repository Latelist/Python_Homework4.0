# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random

k = int(input('Enter power: '))

def random_list(n):
    randoms = []
    for i in range(n+1):
        randoms.append(random.randint(0,100))
    return randoms

def create_polynomial(n, randoms):
    polynomial = ''
    for i in range(n+1):
        if n > 1:
            if randoms[i] == 0:
                polynomial += ''
            else:
                polynomial += f'{randoms[i]}x^{n} + '
        elif n == 1:
            if randoms[i] == 0:
                polynomial += ''
            else:
                polynomial += f'{randoms[i]}x + '
        else:
            if randoms[i] == 0:
                polynomial += '= 0'
            else:
                polynomial += f'{randoms[i]} = 0'
        n -= 1
    return(polynomial)    

randoms = random_list(k)
polynomial = create_polynomial(k, randoms)

with open('file.txt', 'w') as data:
    data.writelines(polynomial)

