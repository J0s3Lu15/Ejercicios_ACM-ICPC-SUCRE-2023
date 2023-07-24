# Paso 1: Leer la cantidad de casos
cantidad_casos = int(input("Ingrese la cantidad de casos a evaluar: "))

# Paso 2: Iterar sobre los casos
for caso in range(cantidad_casos):
    # Leer la hora y los minutos
    hora, minutos = map(int, input("Ingrese la hora y los minutos (en formato HH MM): ").split())

    # Paso 3: Calcular el número formado por la hora y los minutos
    numero = int(str(hora).zfill(2) + str(minutos).zfill(2))

    # Paso 4: Calcular la cantidad de LEDs requeridos
    leds_requeridos = sum([2, 5, 5, 4, 5, 6, 3, 7, 6, 6][int(d)] for d in str(numero))

    # Paso 5: Encontrar el número más grande que se puede formar
    numero_maximo = int("1" * leds_requeridos)

    # Paso 6: Imprimir la cantidad de LEDs requeridos, la hora como un solo número y el número más grande
    print("Para el caso", caso + 1, "la cantidad de LEDs requeridos es:", leds_requeridos)
    print("La hora formada como un solo número es:", numero)
    print("El número más grande que se puede formar es:", numero_maximo)
