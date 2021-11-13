from random import randint
sorteio = list()
print('<<<<< SORTEIO MEGA-SENA >>>>>')
for c in range(0, 6):
    while True:
        numero = randint(1,50)
        if numero not in sorteio:
            sorteio.append(numero)
            break
print(f'Os número sorteados foram {sorteio}')