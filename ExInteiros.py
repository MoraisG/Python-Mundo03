menor = 0
maior = 0
soma = 0
media = 0
tot = 0
while tot >= 0:
    numero = int(input('Digite um número inteiro '))
    if tot == 0:
        menor = numero
        maior = numero
    tot += 1
    soma = soma + numero
    media = float(soma / tot)
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    print('A média é : {}'.format(media))
    print('O menor número é {}'.format(menor))
    print('O maior número é {}'.format(maior))

