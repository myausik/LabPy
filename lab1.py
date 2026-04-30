###Лабораторная работа 1
###Вариант 1
n = 5
k = 3
F = list(range(0, n+1))
F[1] = 1
F[2] = 1

for i in range(3, n + 1):
    F[i] = F[i - 1] + F[i - 2] * k
print(F[n])

###Лабораторная работа 1
###Вариант 2
n = 6
m = 3
agegr = [0] * (m+1)
agegr[0] = 1 #1 пара кроликов возраста 0 месяцев(1ый месяц жизни)
agegr[1] = 1

for i in range(3, n + 1):
    novy = 0
    for j in range(2, m+1):
        novy += agegr[j]

    for l in range(m, 0, -1):
        agegr[l] = agegr[l - 1]
        agegr[0] = novy

vse = 0
for i in range(0, m+1):
    vse += agegr[i]
print(vse)

with open('kroliki2.txt', 'w', encoding='utf-8') as file:
    file.write(f'\nЗадача про кроликов. Вариант 2')
    file.write(f'\nМесяц: {n}')
    file.write(f'\nКролики живут {m} месяцев')
    file.write(f'\nРезультат: всего {vse} пар кроликов')

with open('kroliki2.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)








