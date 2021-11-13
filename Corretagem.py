from operator import itemgetter
info_terreno = dict()
terrenos = list()
for c in range(1, 5):
    info_terreno['numero'] = c
    info_terreno['largura'] = float(input('Informe a largura do terreno (metros): '))
    info_terreno['comprimento'] = float(input('Informe o comprimento do terreno (metros): '))
    info_terreno['area'] = ((info_terreno['largura'] * info_terreno['comprimento']))
    info_terreno['valortotal'] = float(input('Informe o valor total do terreno (R$): '))
    info_terreno['valormetro'] = float(info_terreno['valortotal'] / info_terreno['area'])
    terrenos.append(info_terreno.copy())
print('='*45)
for k, v in enumerate(terrenos):
    print(f'O terreno {v["numero"]} tem {v["area"]} m2 e custa R$ {v["valortotal"]:.1f}')
print('='*45)
ordem = sorted(terrenos, key=itemgetter('valormetro'))
print(f'O terreno {ordem[0]["numero"]} possui o melhor custo beneficio e tem valor de {ordem[0]["valormetro"]:.2f} por m2')