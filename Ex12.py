a = int(input('Digite um número '))
b = int(input('Digite um segundo valor '))
c = int(input('Digite um terceiro valor '))
menor = c
maior = a
if a < c and a < b:
    menor = a
if b < c and b < a:
    menor = b
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O valor {} é o menor'.format(menor))
print('O valor {} é o maior'.format(maior))