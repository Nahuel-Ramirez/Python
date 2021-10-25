# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:14:00 2021

@author: Nahuel Ramirez
"""

import logicaIndices as ind


print("""
¡Bienvenido/a!

A continuacion calcularemos la Tasa Metabolica Basal segun su actividad fisica.
Esto significa que el resultado arrojara el valor de cuantas calorias debe consumir segun su peso, altura, edad, y actividad fisica.
      """)

def ejecCalAct()->float:
    valorGenero = input("""
[+]    Seleccione la opcion:
[+]    Masculino = 0
[+]    Femenino = 1
[*]    Valor = """)
          
    if valorGenero == "0":
        valorGenero = 5
    elif valorGenero == "1":
        valorGenero = -161
    else:
        print("[-] Ingrese una opcion correcta.")
        return print("[-] Error, comience nuevamente")
    
    peso = float(input("[*] Ingrese su peso: "))
    altura = int(input("[*] Ingrese su altura (en cm): "))
    edad = int(input("[*] Ingrese su edad: "))
    
    valorActividad = input("""
[+] Seleccione la opcion:
[+] a : Poco o ningun ejercicio
[+] b : Ejercicio ligero(1 a 3 dias por semana)
[+] c : Ejercicio moderado (3 a 5 dias por semana)
[+] d : Deportista (6-7 dias a la semana)
[+] e : Atleta (entrenamiento mañana y tarde)
[*] Valor = """)

    if valorActividad.lower() == "a":
        valorActividad = 1.2
    elif valorActividad.lower() == "b":
        valorActividad = 1.375
    elif valorActividad.lower() == "c":
        valorActividad = 1.55
    elif valorActividad.lower() == "d":
        valorActividad = 1.72
    elif valorActividad.lower() == "e":
        valorActividad = 1.9
    else:
        print("[-]Ingrese una opcion correcta.")
        return print("[-]Error, comience nuevamente")
                    
    TMBF = ind.caloriasEnActividad(peso, altura, edad, valorGenero, valorActividad)
    return print("\nSu tasa metabolica basal segun su actividad fisica es de: ",TMBF,"cal.")


ejecCalAct()
    
    
    