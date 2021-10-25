# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:33:55 2021

@author: Nahuel Ramirez
"""

import msvcrt
import logicaIndices as ind


print("""[*] A continuacion se le pediran algunos datos que ingresara por consola, que serviran para calcular el porcentaje de grasa corporal.""")
      
      
def ejecPorcGrasa()->float:
    valorGenero = input("""
[+]    Seleccione la opcion:
[+]    Masculino = 0
[+]    Femenino = 1
[+]    Valor = """)
          
    if valorGenero == "0":
        valorGenero = 10.8
    elif valorGenero == "1":
        valorGenero = 0
    else:
        print("[-] Ingrese una opcion correcta.")
        return print("[-] Error, comience nuevamente")
            
        
    
    peso = float(input("[+] Ingrese su peso: "))
    altura = float(input("[+] Ingrese su altura: "))
    edad = int(input("[+] Ingrese su edad: "))
    IMC = ind.calcularIMC(peso, altura)
    GC = ind.calcularPorcGrasa(peso, altura, edad, valorGenero)
    
    return print("\n[*] Su porcentaje de grasa corporal es de: ",GC,"%")
    
    
ejecPorcGrasa()
msvcrt.getch()