texto = input('Digite seu nome: ')
texto = texto.split()
print('O primeiro nome é {} e o último nome {}'.format( texto[0],  texto[len(texto)-1]))

#print('O nome {} possui {}'.format(nome, len(nome.replace(' ', ''))))
#digito = str(input('Digite um valor de 0 a 9999 '))
#i = len(digito)
#print('o número é composto pelos seguintes algarismos: {} , {} , {} '.format(digito[0], digito[1],digito[2]))