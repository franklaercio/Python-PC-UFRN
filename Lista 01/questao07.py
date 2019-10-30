salario = float(input("Informe o seu salário mensal: "))
despesas = float(input("Informe as suas despesas mensais: "))
salarioLiquido = salario - despesas
valorAcumulado = 0
tempo = 0

while(valorAcumulado  <= 1000000):
	valorAcumulado += salarioLiquido
	tempo += 1
else: 
	print("O tempo em anos que irá levar para juntar 1 milhão é: ", round(tempo/12), "anos")
