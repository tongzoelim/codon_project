#DNA에 돌연변이 발생시키는 프로그램(교체)
import random
dnabase = list(input("DNA 서열을 입력하세요: "))
mutation_count = int(input("돌연변이 횟수를 입력하세요: "))
nucleobase = ['A', 'C', 'G', 'T']
for i in range(mutation_count):
    dnabase[random.randint(0,len(dnabase)-1)] = random.choice(nucleobase)
mutated_DNA = ''
for j in range(len(dnabase)):
    mutated_DNA += dnabase[j]
print("돌연변이가 발생한 DNA:", mutated_DNA)