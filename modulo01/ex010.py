"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 3,27
"""
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dol = real / 3.27
print(f'Com R${real:.2f} você pode comprar U${dol:.2f}.')