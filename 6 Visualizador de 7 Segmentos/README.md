# Enunciado:
# 6 Visualizador de 7 Segmentos:

![imagen](https://s3.amazonaws.com/hr-assets/0/1668248508-86f2d53a4f-piedrapapeltijera.png)

Samira es una niña bien curiosa y ha observado el reloj digital de la pared de su casa, y se dio cuenta que las pilas de su reloj se están terminando y algunos leds del reloj no se prenden y forman una hora incorrecta, y se puso a pensar, cuál sería el número más grande(por así decirlo) que se podría formar con los leds que utiliza dicha hora. Por ejemplo se dio cuenta que para que su reloj representa el dígito 8, utiliza todos los leds, es decir 7 leds(según el ejemplo), y ella pensó, que con 7 leds sería posible formar otro número, por ejemplo el 12, ya que el doce necesita 2 leds para el dígito 1 y 5 para el dígito 2, también es posible formar el 13, ya que el 1 utiliza 2 leds y el 3 utiliza 5 leds, y seguramente también podrían formarse el 15 u otras combinaciones posibles, sin embargo, se puso a pensar en cuál sería la combinación que permitiría formar el número más grande posible y se dio cuenta que para el ejemplo anterior, la combinación que forma el número más grande es el 711 ya que el dígito 7 requiere 3 leds, el dígito del medio 1 requiere 2 leds y finalmente el último dígito 1 requiere otros 2 led, sumando la cantidad que requiere cada dígito sería 3+2+2 = 7, que era la cantidad de leds que tiene con el número 8. Para poder guiarte, revisa la imagen superior, un tablero que representa los dígitos numéricos de nuestro sistema, utiliza 7 leds como segmentos de representación, de los cuales, algunos se van encendiendo para representar un dígito, por ejemplo para representar el dígito 1, un tablero debe encender los leds b y c, puedes revisar el resto de los dígitos para darte cuenta. Tu trabajo será identificar el número que se forma en el reloj de Samira como un solo número(es decir uniendo las horas y los minutos) y a partir de ello, identificar cual sería el número más grande que se puede formar con todos los leds que se utiliza para representar dicha hora, por ejemplo si fuesen las 7:30, el número que se forma con esa hora es 730 y la cantidad de Leds que se requieren para representar 730 es 14, con los cuales se podría armar el siguiente número 1111111 con el cual se aprovecharia al maximo todos los leds para formar ese número grande. Considera que para formar el número debes colocar en la posición de las centenas el número que representa la hora y los minutos en las decenas, considerando que si el minutero es de un solo dígito, se debe contemplar que ese dígito tiene a la izquierda el cero de manera complementaria.

Input Format
Inicialmente te facilitarán la cantidad de casos n que se desean evaluar, a continuación la entrada consiste en dos números que representan la hora hh y el minuto mm en formato 24 hrs(Hora Militar, es decir la hora mínima es 00:00 y la máxima 23:59). Considera que el minuto siempre debería representarse con dos dígitos, aunque el que están en posición de las decenas esté apagado, en este caso se asume que a la izquierda del dígito de la unidad lo acompaña un cero)

Constraints
Se garantiza que los valores de la hora y el minutero estan dentro de los valores permitidos en una hora militar.

Output Format
Imprime la cantidad de Leds que se requieren para formar dicha hora, la hora como un solo número y el número más grande que se puede formar con la cantidad de leds obtenidos de la hora anterior por cada caso de prueba..

Sample Input 0
```bash
3
7 30
7 53
14 34
```

Sample Output 0
```bash
14
730
1111111
13
753
711111
15
1434
7111111
```

Sample Input 1
```bash
1
10 14
```

Sample Output 1
```bash
14
1014
1111111
```

## Contactos:
Si te gusta mi trabajo o estás buscando consultoría para tus proyectos, Pentesting, servicios de RED TEAM - BLUE TEAM, implementación de normas de seguridad e ISOs, controles IDS - IPS, gestión de SIEM, implementación de topologías de red seguras, entrenamiento e implementación de modelos de IA, desarrollo de sistemas, Apps Móviles, Diseño Gráfico, Marketing Digital y todo lo relacionado con la tecnología, no dudes en contactarme al +591 75764248 y con gusto trabajare contigo.
