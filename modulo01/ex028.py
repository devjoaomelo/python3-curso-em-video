"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
while True:
    jogador = int(input('Qual número escolhi?')) # chute jogador
    if jogador > 5 or jogador < 0:
        print('Apenas número entre 0 e 5')
        continue
    else:
        break
print('Processando. . .')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você Ganhou!')
else:
    print(f'PERDEU! Eu pensei no número {computador} não no {jogador}!')