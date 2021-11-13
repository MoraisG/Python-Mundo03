#Conversao de bases
n1 = int(input('Informe um número '))
print('''Escolha a base a ser convertida o seu número 
[0] - Opção binária
[1] - Opção Octal
[2] - Opção Hexadecimal''')
opcao = int(input('Informe sua base de conversão '))
if opcao == 0:
    print('{} convertido para binário é {}'.format(n1, bin(n1)[2:]))
elif opcao == 1:
    print('{} convertidado para octal é {}'.format(n1, oct(n1)[2:]))
elif opcao == 2:
    print('{} convertido para hexadecimal é {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção não implementada')