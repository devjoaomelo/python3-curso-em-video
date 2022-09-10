"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep

jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Sua opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)
print('-=' * 12)
print(f'Computador jogou {jogadas[computador]}.')
print(f'Jogador jogou {jogadas[jogador]}.')
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: 
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')