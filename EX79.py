numeros = list()
while True:
    valor = int(input('Digite um número: '))
    if valor in numeros:
        print('O número não foi adicionado')
    else:
        numeros.append(valor)
    parar = str(input('Deseja continuar [S/N]? '))
    if parar in ('nN'):
        break
numeros.sort()
print(f'Os números adicionados foram {numeros}')