#번역 과정 시뮬레이션
import sys
codon_table = [
# A (0)
[
    ['K', 'N', 'K', 'N'],
    ['T', 'T', 'T', 'T'],
    ['R', 'S', 'R', 'S'],
    ['I', 'I', 'M', 'I'],
],
# C (1)
[
    ['Q', 'H', 'Q', 'H'],
    ['P', 'P', 'P', 'P'],
    ['R', 'R', 'R', 'R'],
    ['L', 'L', 'L', 'L'],
],
# G (2)
[
    ['E', 'D', 'E', 'D'],
    ['A', 'A', 'A', 'A'],
    ['G', 'G', 'G', 'G'],
    ['V', 'V', 'V', 'V'],
],
# U (3)
[
    ['*', 'Y', '*', 'Y'],
    ['S', 'S', 'S', 'S'],
    ['*', 'C', 'W', 'C'],
    ['L', 'F', 'L', 'F'],
]
]

thelist = list(input())
acid = 'M'
nucleobase = {'A': 0, 'C': 1, 'G': 2, 'U': 3}
for i in range(len(thelist)):
    thelist[i] = nucleobase[thelist[i]]
start_codon = []
for i in range(3):
    start_codon.append(thelist.pop(0))
try:
    while start_codon != [0, 3, 2]:
        start_codon.pop(0)
        start_codon.append(thelist.pop(0))
except IndexError:
    print('No start codon found')
    sys.exit(0)
for j in range(0,len(thelist),3):
    codon = thelist[j:j+3]
    temporary_codon = codon_table[codon[0]][codon[1]][codon[2]]
    if not temporary_codon == '*':
        acid += temporary_codon
    elif temporary_codon == '*':
        break
print(acid)