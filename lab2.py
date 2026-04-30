###Лабораторная работа 2
###Вариант 2
#Трансляция РНК
table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S',
    'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 'UGC': 'C',
    'UGA': 'Stop', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
    'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R',
    'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I',
    'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T',
    'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V',
    'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A',
    'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
    'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}
RNA = input("Введите РНК-последовательность: ").upper()
#RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

maxLength = 9999
if len(RNA) > maxLength:
    print("Длина РНК превышает 10 килобаз")
    exit()

if len(RNA) % 3 != 0:
    RNA = RNA[:(len(RNA) - len(RNA) % 3)]

protein = ''
for i in range(0, len(RNA), 3):
    codon = RNA[i:i + 3]
    aminoAcid = table.get(codon)
    if aminoAcid is None:
        print(f'Ошибка: неизвестный кодон {codon} в положении {i}')
        break
    if aminoAcid == 'Stop':
        break
    protein += aminoAcid
print(protein)

with open('RNATranslation.txt', 'w', encoding='utf-8') as file:
    file.write(f'\nЗадача на перевод РНК в протеины')
    file.write(f'\nПоследовательность РНК: {RNA}')
    file.write(f'\nПротеиновая последовательность: {protein}')

with open('RNATranslation.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

for i in range(5):
    print(i, end=" ")

or i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")