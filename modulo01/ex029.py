"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você ultrapassou o limite permitido que é: 80 Km/h!')
    multa = (v - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Você está dentro da velocidade permitida')
print('Drive safe!')