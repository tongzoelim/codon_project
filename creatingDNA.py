#DNA 생성 프로그램
import random
length = int(input("DNA의 길이를 입력하세요: "))
nucleobases = ['A', 'C', 'G', 'T']
dna_sequence = ''
for a in range(length):
    dna_sequence += random.choice(nucleobases)
print("생성된 DNA 서열:", dna_sequence)