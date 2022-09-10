"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

atual = date.today().year
ano = int(input('Digite seu ano de nascimento'))
idade = atual - ano
if idade == 18:
    print('Está na hora de se alistar')
elif idade < 18:
    restante = 18 - idade
    print(f'Você ainda vai se alistar\n Seu alistamento será em {restante} anos')
elif idade > 18:
    restante = idade - 18
    print(f'Já passou do tempo de alistamento\n Você deveria ter se alistado {restante} anos atrás em {atual - 8}')