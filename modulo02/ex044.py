"""
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
preco = float(input('Qual o preço do produto? '))
print('')
print('[ 1 ] À vista no dinheiro/cheque\n[ 2 ] À vista no cartão\n[ 3 ] Em até 2x no cartão\n[ 4 ] ou mais no cartão\n')
opcao = int(input('selecione a opção de pagamento? '))
if opcao == 1:
    print(f'O produto de valor R${preco} sairá por R${preco * 0.9} (10% de desconto)')
elif opcao == 2:
    print(f'O produto de valor R${preco} sairá por R${preco * 0.95} (5% de desconto)')
elif opcao == 3 or 4:
    parcela = int(input('Quantas vezes no cartão?'))
    if parcela <= 2:
        print(f'O produto sairá pelo valor de R${preco} (sem desconto)')
    elif parcela > 2:
        total = preco * 1.2
        print(f'Cada parcela sairá por R${total/parcela} valor total = R${total} (20% de juros) ')
