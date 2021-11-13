genero = input('Informe o SEXO [M/F] da pessoa: ').strip().upper()[0]
while genero not in 'mMfF':
    genero = input('Informe o genero da pessoa ').strip().upper()[0]
print('Genero informado corretamente')