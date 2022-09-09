"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

distancia = float(input('Digite a distância da viagem em km: '))
if distancia > 0 and distancia <= 200: 
    preco = distancia * 0.5
    print(f'O preço dessa viagem foi de R${preco:.2f}')
elif distancia > 200:
    preco = distancia * 0.45
    print(f'O preço dessa viagem longa foi de R${preco:.2f}')
else:
    print('Distância inválida')