aluno = dict()
aluno['nome']= str(input('Informe o nome do aluno: '))
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'em recuperacao'
for k, v in aluno.items():
    print(f'{k} é {v}')