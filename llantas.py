# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:22:02 2020

@author: POINT
"""


"""
Calcular el valor total que una persona debe pagar por la compra de llantas en un almacén
que tiene la siguiente promoción: Si la cantidad de llantas comprada es mayor a 4, el
precio unitario tiene un descuento de 10%. El programa debe ingresar como datos la
catidad de llantas y el precio inicial de cada llanta. Mediante una comparación el programa
deberá aplicar el descuento.

Prueba del programa
>>>
Cantidad de llantas: 3
Precio unitario: 80
Valor a pagar: 240.0
Cantidad de llantas: 5
Precio unitario: 80
Valor a pagar: 360.0
"""
"""
nombre: Monteros Mejia Jhonatan
grupo: Nº10
"""

llantas=input("Cantidad de llantas: ")
llantas=int(llantas)
print ("precio unitario: 80")

if llantas<=4:
    result=llantas*80
    result=float(result)
    print("valor a pagar: ",result)
    
else:
    result2=(llantas*80)*0.9
    result2=float(result2)
    print("valor a pagar: ",result2)
    
    
    


