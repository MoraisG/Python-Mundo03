salario = float(input('Informe seu salário '))
prestacao = float(input('Qual o valor da prestação? '))
if prestacao <= (salario*0.2):
    print('Empréstimo concedido'.format(prestacao))
else:
    print('Empréstimo não concedido')
