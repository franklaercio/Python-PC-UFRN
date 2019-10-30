saldo = 1000

opcao = int(input("1 SAQUE \n","2 DEPÓSITO \n", "3 SALDO \n"))

if opcao == 1:
	valorSaque = float(input("Informe o valor que deseja sacar: "))
	if valorSaque <= saldo
		print("Saque autorizado!")
		print("Saldo atual: ", saldo - valorSaque)
elif opcao == 2:
	valorDeposito = float(input("Informe o valor que deseja depositar: "))
	if valorDeposito > 0
		print("Depósito realizado!")
		print("Saldo atual: ", saldo + valorDeposito)
elif opcao == 3:
	print("Saldo atual: ", saldo)
	print("Obrigado por nos consultar!")
else:
	print("Opção inválida!")