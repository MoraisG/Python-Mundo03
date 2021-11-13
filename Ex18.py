n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe um segundo número inteiro: '))
lista = ''
inicio = int(n1)
final = int(n1)
if n1 != n2:
    if n2 < inicio:
        inicio = n2
    if n2 > final:
        final = n2
    while inicio != final:
        if inicio % 2 != 0:
            if lista == '':
                lista = str(inicio)
            else:
                lista = lista + ' ' + str(inicio)
        inicio += 1
    print('Os números ímpares entre {} e {} são: {}'.format(n1, n2, lista), end='')
else:
    print('Os números informados são iguais')