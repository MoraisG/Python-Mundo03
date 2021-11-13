princ = list()
temp = list()
maior = menor = 0
while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(float(input('Informe o peso dela: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = input('Deseja parar? ')
    if r in 'sS':
        break
print(f'Foram cadastrados ao todo {len(princ)}')
print(f'O maior peso são de:', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} com {p[1]}Kg', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'O menor peso é de {p[0]} com {p[1]}Kg')


