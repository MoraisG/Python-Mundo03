from random import randint
from time import sleep
computador = randint(0,10)
print('O computador está PENSANDO em um número de 0 a 10')
print('-=-' * 20)
n1 = int(input('Informe um número: '))
print('Processando....')
sleep(5)
print('-=-'*20)
if computador == n1:
    print('Parabéns você venceu')
else:
    print('Ihhhh não foi desta vez')

