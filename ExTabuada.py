nome = input('Cadastre um usuário: ')
senha = input('Cadastre uma senha: ')
while nome == senha:
    senha = input('Cadastre um senha diferente: ')
print('Informações validadas com sucesso!')