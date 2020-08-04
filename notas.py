# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:54:25 2020

@author: POINT
"""
"""
Durante el semestre un estudiante debe realizar tres evaluaciones. Cada evaluación 
tiene una calificación y la nota total que recibe el estudiante es la suma de las dos 
mejores calificaciones
Escriba un programa que lea las tres calificaciones y determine cual es la 
calificación total que recibirá el estudiante.
DATOS DE PRUEBA
Ingrese su primera calificación: 75
Ingrese su segunda calificación: 68
Ingrese su tercera calificación: 82
Su calificación total es: 157
"""

nota1=(int(input("ingrese su primera calificación: ")))
nota2=(int(input("ingrese su segunda calificación: ")))
nota3=(int(input("ingrese su tercera calificación: ")))

if nota1>nota3 and nota2>nota3:
    suma1=nota1+nota2
    print("su calificación es:",suma1)
elif nota1>nota2 and nota3>nota2:
    suma2=nota1+nota3
    print("su calificación final es: ",suma2)
elif nota2>nota1 and nota3>nota1:
    suma3=nota2+nota3
    print("su calificación final es: ",suma3)
