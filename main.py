'''A sequência de Fibonacci é uma sequência de números, onde o número 1 é o primeiro e segundo termo da ordem e os demais são originados pela soma de seus antecessores.'''

numero_1 = 0  # Primeiro número da sequência Fibonacci é 0
numero_2 = 1 # O segundo número da sequência é 1
numero_3 = 1 # O terceiro número é a soma dos dois primeiros números. (0+1 = 1)

numeros_fibonacci = [0, 1, 1] # Para que de certo, é necessário adicionar os valores iniciais na lista, pois é de boa prática evitar funções desnecessárias


retangulo_de_ouro = ['None', '1', '2'] # O retângulo de ouro é a divisão do último número por seu antecessor, a partir do número 3, pode-se perceber que a divisão passa a dar 1,6. Por isso esse valor é chamado de divina divisão


for i in range(10):
	numero_1 += numero_2 # O primeiro número soma com o segundo
	numero_2 += numero_3 # O segundo soma com o terceiro número
	numero_3 = numero_1 + numero_2 # O terceiro número passa a ser a soma dos dois anteriores

	divina_proporcao = f'{numero_3 / numero_2:3f}' # A divina proporção se baseia em divir o último número com seu anterior e a partir do número 3

	
	numeros_fibonacci.append(numero_2) # Adiciona o segundo número na sequência
	numeros_fibonacci.append(numero_3) # Adiciona o terceiro número na sequência
	retangulo_de_ouro.append(divina_proporcao)

print(f'{numeros_fibonacci}\n') # Printa a lista com todos os números
print(retangulo_de_ouro) # Printa o retângulo de ouro, divisão do último valor por seu valor anterior
