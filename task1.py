import random
# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = int(input())
p = 1
while p <= n:
    print(p, end = ' ')
    p = p * 2
                
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

numberX = random.randint(0, 1000)
numberY = random.randint(0, 1000)
s = numberX + numberY
p = numberX * numberY
print(f"Сумма этих чисел: {s}")
print(f"Произведение этих чисел: {p}")
print(*sorted([numberX, numberY]))

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

quantityEagle = random.randint(1, 5)
quantityTails = random.randint(1, 5)
print(quantityEagle)
print(quantityTails)
if quantityEagle > quantityTails:
    print(quantityTails)
else:
    print(quantityEagle)
