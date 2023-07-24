n = int(input())
if 2 <= n <= 10**10:
	cartas = input()
	cartas = cartas.split()
	cartas = list(map(int, cartas))
	for i in range(1, n+1):
		print(i)
		if i not in cartas:
			print(i)
			break