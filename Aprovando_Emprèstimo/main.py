casa = float(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos você vai pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {}'.format(casa, anos), end ='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')