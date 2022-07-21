emprestimo = float(input('Digite o valor do emprestimo: R$'))
salario = float(input('Quanto você ganha? R$'))
anos = int(input('Quantos anos de financiamento? R$'))
prestacao = emprestimo / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma emprestimo de R${emprestimo} em {anos}anos')
print(f'A prestação sera de R${prestacao}')

if prestacao <= minimo:
    