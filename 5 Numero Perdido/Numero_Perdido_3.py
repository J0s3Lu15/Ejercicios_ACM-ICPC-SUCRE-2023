import random
n = int(input())
cartas = []
if n >= 2 and n <= 10:
	#print(n)
	i = 1
	while i <= n:
		cartas.append(i)
		i = i + 1
	x = random.randint(1,n)
	cartas.remove(x)
	random.shuffle(cartas)
	cart = " ".join(map(str, cartas))
	print(cart)

	while True:
		respuesta = int(input())
		if respuesta == x:
			break