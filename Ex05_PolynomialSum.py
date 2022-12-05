# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

def split_polynomial(polynomial):
    fractions = polynomial.split(' ')
    return fractions

def remove_irrelevant(list):
    list.remove('0')
    for i in list:
        if (i == '+') or (i == '='):
            list.remove(i)
    return list

def create_matrix(list):
    for i in range(len(list)):
        list[i] = list[i].split('x')

def complete_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '':
                matrix[i][j] = '1'
            if len(matrix[i]) == 1:
                matrix[i].append('^0')

def find_common_power(matrix):
    common_power = False
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][1] == matrix[j][1] and i != j:
                common_power = True
            elif j == len(matrix) - 1 and common_power == False:
                results.append(matrix[i])

def get_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][1] == matrix[j][1]:
                matrix[i][0] = int(matrix[i][0])
                matrix[j][0] = int(matrix[j][0])
                sum = matrix[i][0] + matrix[j][0]
                results.append([str(sum), matrix[i][1]])

path1 = 'polynomial1.txt'
path2 = 'polynomial2.txt'

with open(path1, 'r') as data:
    polynomial1 = data.readline()

with open(path2, 'r') as data:
    polynomial2 = data.readline()

print(polynomial1)
print(polynomial2)

fractions1 = remove_irrelevant(split_polynomial(polynomial1))
fractions2 = remove_irrelevant(split_polynomial(polynomial2))
all_fractions = fractions1+fractions2

create_matrix(all_fractions)
complete_matrix(all_fractions)

results = []
find_common_power(all_fractions)
get_sum(all_fractions)


answer = ''
for i in range(len(results)):      
    if results[i][1] == '1':
        answer += f'{results[i][0]}x + '
    elif results[i][1] == '^0':
        answer += f'{results[i][0]} = 0'
    else:
        answer += f'{results[i][0]}x{results[i][1]} + '

print(answer)
with open('polynomialsum.txt', 'w') as data:
    data.writelines(answer)


