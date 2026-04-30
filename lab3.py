###Лабораторная работа 3
##Задание 2
#Построение графика динамики временных рядов

import matplotlib.pyplot as plt
from statsmodels.datasets import elnino

data = elnino.load_pandas()
el = data.data
#print(el.head())

el_1990_2010 = el[(el['YEAR'] >= 1990) & (el['YEAR'] <= 2010)]
#print(el_1990_2010)
months = data.names[1:]

plt.figure(figsize=(24, 6))
for i in months:
    plt.plot(el_1990_2010['YEAR'], el_1990_2010[i], '-*', label=i)
plt.xlabel('Год')
plt.ylabel('Температура')
plt.title('Эль-Ниньо (1990-2010)')
plt.legend(loc='upper right', ncol = 4)
plt.grid(True)
plt.savefig('elnino.png')
plt.show()