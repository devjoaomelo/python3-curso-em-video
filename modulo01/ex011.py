"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

lar = float(input('Digite a largura: (em Metros) '))
alt = float(input('Digite a altura: (em Metros)'))
area = lar * alt
litro = area / 2

print(f'Uma parede de dimensão de {lar}m x {alt}m tem uma área de {area:.2f}m²\nPara pintar essa parede, precisará de {litro} litros de tinta.')