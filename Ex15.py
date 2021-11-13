n1 = int(input('Informe um número inteiro '))
n2 = int(input('Informe um segundo número inteiro '))
if n1 > n2:
    print('{} é maior que {} '.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {} '.format(n2, n1))
else:
    print('Os números são iguais')