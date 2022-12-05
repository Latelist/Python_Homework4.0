# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

import math
from decimal import Decimal
accuracy = (input('Enter accuracy degree: '))

try:
    check = Decimal(accuracy)
    if accuracy[-1] == '1' and ((accuracy[-2]== '0') or (accuracy[-2] == '.')):
        accuracy = len(accuracy) - 2
        pi = round(math.pi, accuracy)
        print(pi)
    else:
        print('Incorrect accuracy degree')
        
except:
    print('Incorrect accuracy degree')