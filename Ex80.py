lista = list()
for c in range(0, 5):
    numero = int(input('Digite um número inteiro: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
