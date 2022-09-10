"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""
numero = int(input('Digite um número inteiro: '))
opcao = int(input('[ 1 ] converter para binário\n[ 2 ] converter para octal\n[ 3 ] converter para hexadecimal'))
if opcao == 1:
    print(f'O número {numero} convertido para é {bin(numero)[2:]}')
if opcao == 2:
    print(f'O número {numero} convertido para é {oct(numero)[2:]}')
if opcao == 3:
    print(f'O número {numero} convertido para é {hex(numero)[2:]}')
