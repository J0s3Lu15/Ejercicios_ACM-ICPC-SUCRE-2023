while True:
    hora, minuto = map(str, input().split())
    if hora == "0" or minuto == "0":
            break
    horaint = int(hora)
    minutoint = int(minuto)
    if horaint <= 23 and horaint >= 0 and minutoint <= 59 and minutoint >= 0 or hora == "00" or minuto == "00":
        hora_invertida = hora[::-1]
        if hora_invertida == minuto:
            print("SI")
        else:
            print("NO")
    else:
        break