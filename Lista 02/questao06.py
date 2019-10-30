valorCompra = float(input("Informe o valor da compra: "))

opcao = str(input("V – para pagamento à vista ou P – para pagamento parcelado"))

if opcao == "V":
	compraDesconto = valorCompra - (valorCompra*0.05)
	print("O valor da compra à vista é: ", compraDesconto)		
if opcao == "P":
	compraParcelada = valorCompra + (valorCompra*0.08)
	print("O valor da compra parcelada é: ", compraParcelada)		

print("O valor da compra é: ", valorCompra)		

