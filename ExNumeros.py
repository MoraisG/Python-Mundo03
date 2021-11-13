for c in range(1, 11):
    numero = int(input('Informe o {}ª número: '.format(c)))
    if c == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('O maior e menor números da lista foram {} e {}, respectivamente '.format(maior, menor))