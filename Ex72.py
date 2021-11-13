#Tuplas
count = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quartoze', 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20 '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente')
print(f'Você digitou o valor {count[numero]}')
while True:
    continuar = str(input('Deseja continuar? '))
    if continuar in 'Sim,S,s':
        numero = int(input('Digite um número entre 0 e 20 '))
        if 0 <= numero <= 20:
            print(f'Você digitou o valor {count[numero]}')
        print('Tente novamente')
    else:
        break
print('Fim de jogo')
