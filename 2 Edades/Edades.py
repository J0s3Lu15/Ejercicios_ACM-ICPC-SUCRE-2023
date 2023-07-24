nacimiento_dia, nacimiento_mes, nacimiento_anio = map(int, input().split())
evaluacion_dia, evaluacion_mes, evaluacion_anio = map(int, input().split())
if 1 <= nacimiento_dia <= 30 and 1 <= nacimiento_mes <= 12 and 1 <= evaluacion_dia <= 30 and 1 <= evaluacion_mes <= 12:
    edad_aproximada = evaluacion_anio - nacimiento_anio
    if evaluacion_mes < nacimiento_mes or (evaluacion_mes == nacimiento_mes and evaluacion_dia < nacimiento_dia):
        edad_aproximada -= 1
    print(edad_aproximada)