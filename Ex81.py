princ = list()
pares = list()
impares = list()
while True:
    princ.append(int(input('Digite um número inteiro: ')))
    r = str(input('Deseja continuar? '))
    if r in 'nN':
        break
for k, v in enumerate(princ):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(pares)
print(impares)