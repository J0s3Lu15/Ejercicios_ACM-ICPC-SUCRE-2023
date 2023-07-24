try:
    n = int(input())
    if 2 <= n <= 10**10:
        cartas = input()
        cartas = cartas.split()
        cartas = list(map(int, cartas))

        xor_total = 0
        xor_acumulado = 0

        for i in range(1, n + 1):
            xor_total ^= i

        for num in cartas:
            xor_acumulado ^= num

        x = xor_total ^ xor_acumulado

        print(x)
except ValueError:
    exit()