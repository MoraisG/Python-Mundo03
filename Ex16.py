nota = int(input('Informe sua nota: '))
faltas = int(input('Informe o número de faltas: '))
if faltas <= 10:
    if 85 <= nota <= 100:
        print('Seu coneito na disciplina foi A')
    elif 60 <= nota <= 84:
        print('Seu conceito na disciplina foi B')
    elif 0 <= nota <= 59:
        print('Seu conceito na disciplina foi C')
else:
    if 85 <= nota <= 100:
        print('Seu conceito na disciplina foi B')
    elif 60 <= nota <= 84:
        print('Seu conceito na disciplina foi C')
    elif 0 <= nota <= 59:
        print('Seu conceito na disciplina foi D')