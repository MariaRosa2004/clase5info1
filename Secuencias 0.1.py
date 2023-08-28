# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 07:22:20 2023

@author: josem
"""
a=int(input("Escribe un numero: "))
b=int(input("Escribe un numero: "))
c=int(input("Escribe un numero: "))

if a<b<c:
    print("Los numeros de forma descendente", c,b,a)
elif b<a<c:
    print("Los numeros de forma descendente", b,a,c)
elif c<b<a:
    print("Los numeros de forma descendente", a,b,c)
elif a<c<b:
    print("Los numeros de forma descendente", b,c,a)
elif b<c<a:
    print("Los numeros de forma descendente", a,c,b)
elif c<a<b: 
    print("Los numeros de forma descendente", b,a,c)
