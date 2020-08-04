# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:24:39 2020

@author: POINT
"""



nombre=input("ingrese su nombre: ")
print("\n"*1)
apellido=input("ingrese su apellido: ")
print("\n"*1)
edad=input("ingrese su edad: ")

print("\n"*1)
if edad >=0 and edad <=11:
    print("aun eres un niño")
elif edad >=12 and edad <=18:
    print("eres un adolescente")
elif edad >=18 and edad <= 59:
    print("usted es un adulto")
else:
    print ("tercera edad")   
print("\n"*1)
ubicacion=input("ingrese su ubicacion: ")
print("\n"*1)
print("hola "+nombre+" "+apellido+", bienvenido.")
print("su edad es "+edad+" años")
print("su ubicacion actual es "+ubicacion)
print("\n"*1)
edad=int(edad)
if edad >=0 and edad <=11:
    print("aun eres un niño")
elif edad >=12 and edad <=18:
    print("eres un adolescente")
elif edad >=18 and edad <= 59:
    print("usted es un adulto")
else:
    print ("tercera edad")

      