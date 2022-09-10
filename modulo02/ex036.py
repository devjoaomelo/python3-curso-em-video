"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""
valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
anos = int(input('Será pago em quantos anos?'))

limite = salario * 0.3
prestacao = valor_casa / (anos * 12)

if prestacao <= limite:
    print(f'Crédito aprovado\nSua prestação será dê R${prestacao}')
else:
    print(f'Crédito negado!')