# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:14:06 2020

@author: POINT

"""
"""
Nombre: Monteros Mejia Jhonatan
Grupo: Nº10
"""
"""

Para el pago semanal a un obrero se consideran los siguientes datos: horas trabajadas,
tarifa por hora y descuentos. Si la cantidad de horas trabajadas en la semana es mayor a
40, se le debe pagar las horas en exceso con una bonificación de 50% adicional al pago
normal. 
Prueba del programa
Horas trabajadas: 45
Tarifa por hora: 4
Descuentos 40
Valor a pagar 150.0

"""
horastrabajo=int(input("horas trabajadas: "))
tarifa=int(input("tarifa por hora: "))
if horastrabajo<=40:
    salario1=horastrabajo*tarifa
    descuento1=(salario1-40)
    print("Descuento: 40")
    print("Valor a pagar: ",descuento1)
else:
    tarifaextra=tarifa+0.5*tarifa
    horasextra=horastrabajo-40
    salario2=horasextra*tarifaextra+40*tarifa
    descuento2=(salario2-40)
    print("Descuento: 40")
    print("Valor a pagar: ",descuento2)

           