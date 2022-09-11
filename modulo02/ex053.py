"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

palavra = str(input('Digite uma frase: ')).upper()
palavra = ''.join(palavra.split())
print(palavra)
if palavra == ''.join(reversed(palavra)):
    print('Palindromo')
else:
    print('Não é um palindromo')
