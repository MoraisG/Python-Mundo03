jogador = dict()
gols = list()
jogador['nome'] = str(input('Informe o nome do jogador: '))
totalPartidas = int(input(f'Quantas partidas o {jogador["nome"]} participou: '))
for c in range(0, totalPartidas):
    gols.append(int(input(f'Quantos gols o jogador {jogador["nome"]} fez na partida n° {c}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print(f'O jogador {jogador["nome"]} participou em {len(jogador["gols"])} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'O jogador {jogador["nome"]} fez em {v} gol na partida {k}')
print(f'O jogador {jogador["nome"]} fez um total de {jogador["total"]}')