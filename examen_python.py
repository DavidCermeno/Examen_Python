# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:38:57 2021

@author: Licht
"""

# Examen Python
# En una llantera se ha establecido una promoción de las llantas marca
# Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos
# de cinco llantas el precio es de $300 cada una, de $250 si se compran de
# cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero
# que una persona tiene que pagar por cada una de las llantas que compra y la
# que tiene que pagar por el total de la compra.

clla = int(input('Digite la cantidad de llantas a comprar: '))
p1 = 300
p2 = 250
p3 = 200
if clla < 5:
    f = p1 * clla
    p = p1
elif clla >= 5 and clla <= 10:
    f = p2 * clla
    p = p2
else:
    f = p3 * clla
    p = p3
print(f'Por cada llanta debe pagar el valor de: ${p}')
print(f'La cantidad total de dinero a pagar es de: ${f}')


# Hacer algoritmo que de el valor final por la compra de televisores. El
# descuento lo hace basado en los dos numeros finales a la cédula, si
# termina en 01 el descuento es del 10% y si termina en 25 el descuento es
# del 20%, si termina en 44 el descuento es 35% y si es 57 el 50%

vc = float(input('Digite valor de la compra: '))
nc1 = int(input('Digite el penúltimo número de su cédula: '))
nc2 = int(input('Digite el último número de su cédula: '))
if nc1 == 0 and nc2 == 1:
    f = vc * 0.90
else:
    if nc1 == 2 and nc2 == 5:
        f = vc * 0.80
    else:
        if nc1 == 4 and nc2 == 4:
            f = vc * 0.65
        else:
            if nc1 == 5 and nc2 == 7:
                f = vc * 0.50
            else:
                f = vc
print(f'El valor de la compra es de: {vc}')
print(f'El valor de la compra con descuento es de: ${f}')


# Una empresa de colchones ofrece descuento según la siguiente tabla
# Numero de colchones comprados % Descuento
# De 0 a menos de 3              0%
# De 3 hasta menos de 6          20%
# De 6 hasta menos de 8          25%
# De 8 en adelante               30%

cc = int(input('Digite el número de colchones comprados: '))
d1 = 0
d2 = 20
d3 = 25
d4 = 30
if 1 >= cc < 3:
    p = d1
else:
    if 3 >= cc < 6:
        p = d2
    else:
        if 6 >= cc < 8:
            p = d3
        else:
            p = d4
print(f'El descuento aplicado por la compra de {cc} colchones')
print(f'es de {p}%')

# Una universidad desea seleccionar una muestra de estudiantes para
# realizar una encuesta. Si el número de estudiantes es menor que 20 se
# tomará el 50%, si el salón tiene entre 20 y 30 estudiantes se tomará 60%,
# si la cantidad es mayor a 30 tomará 70%. ¿Que cantidad de estudiantes
# serán seleccionados para la encuesta?.

ce = int(input('Digite la cantidad de estudiantes para la muestra: '))
c1 = 0.50
c2 = 0.60
c3 = 0.70

if ce < 20:
    f = ce * c1
    ff = round(f)
elif ce >= 20 and cc <= 30:
    f = ce * c2
    ff = round(f)
else:
    f = ce * c3
    ff = round(f)
print(f'La cantidad de estudiantes seleccionados para la encuestas es: {ff}')




















