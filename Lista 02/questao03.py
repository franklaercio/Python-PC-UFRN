nome = str(input("Informe o seu nome: "))
sexo = str(input("Informe o seu sexo se é masculino ou feminino: "))

if sexo =="masculino":
	print("Bem vindo Ilmo Sr.", nome)
elif sexo =="feminino":
	print("Bem vinda Ilmo Sra.", nome)
else: 
	print("Sexo inválido!\n","Digite extamante masculino ou feminino")		

