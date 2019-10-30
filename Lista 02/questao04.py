salario = float(input("Informe o seu salário: "))
valorFinanciamento = float(input("Informe o valor do financiamento pretendido: "))

if valorFinanciamento <= 5*salario: 
	print("Financiamento concedido!")
else:
	print("Financiamento negado!")
	
print("Obrigado por nos consultar!")	