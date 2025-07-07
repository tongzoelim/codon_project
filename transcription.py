#전사과정 시뮬레이션 프로그램
acid_list = {'A':'U', 'C':'G', 'G':'C', 'T':'A'}
DNA_list = input()
RNA_list = ''
for a in DNA_list:
    RNA_list += acid_list[a]
print(RNA_list)