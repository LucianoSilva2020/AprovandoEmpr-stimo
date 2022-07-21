emprestimo = float(input('Digite o valor do empréstimo: R$'))
salario = float(input('Quanto você ganha? R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = emprestimo / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma empréstimo de R${emprestimo} em {anos} anos')
print(f'A prestação sera de R${prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!!')
else:
    print('Empréstimo NEGADO!!')    