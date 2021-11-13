#Jogo de dados;
from random import  randint
from time import  sleep
from operator import  itemgetter
jogo = {
    'jogadorUm': randint(1, 6),
    'jogadorDois': randint(1, 6),
    'jogadorTres' : randint(1, 6),
    'jogadorQuatro' : randint(1, 6)
}
ranking = list()
print('Os dados foram')
for k, v in jogo.items():
    print(f'O {k} tirou o dado com valor {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, d in enumerate(ranking):
    print(f'{i+1}° lugar {d[0]} tirou o dado {d[1]}')
