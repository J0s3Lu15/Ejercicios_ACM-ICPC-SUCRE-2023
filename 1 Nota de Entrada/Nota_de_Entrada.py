nl = float(input())
t = float(input())
ep = float(input())
if (nl>=0 and nl <= 100) and (t>=0 and t <= 100) and (ep>=0 and ep <= 100):
	nl = 25*nl/100
	t = 10*t/100
	ep = 30*ep/100
	Entrada = float("{:.1f}".format(nl+t+ep))
	Minimo = float("{:.1f}".format(51-(nl+t+ep)))
	print("Entrada =",Entrada)
	print("Minimo =",Minimo)