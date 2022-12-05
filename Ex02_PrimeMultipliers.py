# Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.

def simplicity_check(number):
    is_prime = False
    for i in range(2, number+1):
        if number % i == 0:
            if number == i:
                is_prime = True
            break
    return is_prime

def simple_multiplier(number):
    answer = []
    if simplicity_check(number) == True:
        answer = f'Number {number} is prime and has no prime multipliers'
    else:
        for i in range(1, number):
            if (number % i == 0) and (simplicity_check(i) == True):
                answer.append(i)
        answer = tuple(answer)
    return answer


N = int(input('Enter natural number: '))
print(simple_multiplier(N))


    