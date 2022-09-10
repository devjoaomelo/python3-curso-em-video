"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso')
elif 25 > imc >= 18.5:
    print('Peso ideal')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 > imc >= 30:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
