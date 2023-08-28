# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:54:46 2023

@author: josem
"""
esferauno=int(input("Ingrese densidad de la esfera 1"))
esferados=int(input("Ingrese densidad de la esfera 2"))
esferatres=int(input("Ingrese densidad de la esfera 3"))

if esferauno>esferados>esferatres:
    print("La esfera 1 es de mayor densidad")
elif esferauno>esferatres>esferados:
    print("La esfera 1 es de mayor densidad")
elif esferados>esferatres>esferauno:
    print("La esfera 2 es de mayor densidad")
elif esferados>esferauno>esferatres:
    print("La esfera 2 es de mayor densidad")
elif esferatres>esferados>esferauno:
    print("La esfera 3 es de mayor densidad")
elif esferatres>esferauno>esferados:
    print("La esfera 3 es de mayor densidad")
