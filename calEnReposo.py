# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:09:52 2021

@author: Nahuel Ramirez
"""
import msvcrt
import logicaIndices as ind


print("""
¡Bienvenido/a!

A continuacion, calcularemos su Tasa Metabolica Basal, esto es minimo de calorias necesarias para vivir.
Calcularemos el numero de calorias que tu cuerpo quema al estar en reposo.
      """)
      
def ejectCalRep()->float:
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
    altura = float(input("[*] Ingrese su altura (en cm): "))
    edad = int(input("[*] Ingrese su edad: "))
    
    TMB = ind.caloriasEnReposo(peso, altura, edad, valorGenero)
    return print("[+]Su Tasa Metabolica Basal es: ",TMB,"cal.")

ejectCalRep()
msvcrt.getch()
    
    
    
    
    
    
    
    
    
    
    