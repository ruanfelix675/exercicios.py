dici = {}
for i in range(3):
    aluno = input('digite seu nome:')
    nota = int(input('digite sua nota:'))
    dici.update({aluno:nota})
for i in dici:
    print(f'aluno - {i} {dici.values()}')
