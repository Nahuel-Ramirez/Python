# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:39:48 2021

@author: Usuario
"""

import msvcrt
import logicaIndices as ind

print("Bienvenido/a, a continuacion, se le pedira peso(kg) y altura(m) para calcular su indice de masa corporal.")


def ejecIMC()->float:
    peso=float(input("Ingrese su peso: "))
    altura=float(input("Ingrese su altura: "))
    IMC = ind.calcularIMC(peso, altura)
    return print("Su indice de masa corporal es de: ",IMC)

ejecIMC()
msvcrt.getch()
