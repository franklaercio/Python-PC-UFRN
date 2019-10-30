contador = 0
numero = 0
maior = 0
menor = 0

while(contador < 4):
	numero = int(input("Informe um número: "))

	if contador == 0:
		maior = numero
		menor = numero
	if numero < menor:
		menor = numero
	if numero > maior:
		maior = numero

	contador += 1
else:
	print("--------------------------")
	print("O maior número é: ", maior)
	print("O menor número é: ", menor)				
	