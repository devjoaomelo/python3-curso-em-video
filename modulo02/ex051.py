"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
p = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
decimo = p + 9 * ra
for c in range(p, decimo + ra, ra):
    print(f'{c}', end=' -> ')
print('ACABOU')