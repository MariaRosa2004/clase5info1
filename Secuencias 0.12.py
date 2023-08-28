# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:22:58 2023

@author: josem
"""

nombre=input("Ingrese Nombre y Apellidos ")
numero_de_inscripcion=int(input("Ingrese numero de inscripcion "))
patrimonio=int(input("Ingrese su patrimonio "))
estrato=int(input("Ingrese estrato al que pertenece "))

if patrimonio<2000000 and estrato<3:
    matricula=50000
    print("Estudiante "+nombre+"no°"+numero_de_inscripcion+"la matricula que debera pagar es del valor: "+ matricula+"$")
elif patrimonio >2000000 and estrato<3:
    matricula=50000
    print("Estudiante "+nombre+"no°"+numero_de_inscripcion+"la matricula que debera pagar es del valor: "+ matricula+"$")
elif patrimonio>2000000 and estrato>3:
    matricula=50000 + patrimonio*0.03
    print("Estudiante "+nombre + " no° de inscripcion: " + str(numero_de_inscripcion)+" la matricula que debera pagar es del valor: "+ str(matricula)+"$")
    
    
