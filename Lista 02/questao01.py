anoNascimento = int(input("Informe o seu ano de nascimento: "))
idade = 2019 - anoNascimento

if idade >= 16:
	print("Você possue idade para votar!")
if idade >= 18:
	print("Você possue idade para tirar a CNH!")
