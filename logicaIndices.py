# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:26:30 2021

@author: Nahuel Ramirez
"""

def calcularIMC (peso:float, altura:float)->float():
    """
    se utiliza para estimar si el peso de
    una persona es adecuado con respecto a su altura. 
    El IMC se calcula como la razón entre el peso en kilogramos y
    el cuadrado de la altura en metros de la persona:
    """
    IMC = peso/(altura)**2
    return round(IMC, 2)
    

def calcularPorcGrasa(peso:float, altura:float, edad:int, valorGenero:float)->float:
    """permite establecer si una persona tiene un nivel
adecuado o excesivo de grasa en su cuerpo. Este se calcula a partir del IMC, la edad y el género de la persona.
valorGenero = 10.8 en Masculino, 0 en Femenino.
    """
    IMC = calcularIMC(peso,altura)
    GC = 1.2 * IMC + 0.23 * edad - 5.4 - valorGenero
    return round(GC, 2)
    


def caloriasEnReposo(peso:float,altura:int,edad:int,valorGenero:float)->float:
    """
    La tasa metabólica basal es el mínimo de calorías necesarias para vivir 
    es decir el número de calorías que un ser
    humano quema al día estando en reposo.
    
    valorGenero = 5 Masculino, -161 femenino.
    """
    TMB = (10*peso)+(6.25*altura)-(5*edad)+valorGenero
    return round(TMB, 2)
    
    

def caloriasEnActividad(peso:float, altura:int, edad:int, valorGenero:float, valorActividad:float)->float:
    """Para poder calcularlo es necesario multiplicar el TMB por un valor que
depende de la actividad física semanal que realiza cada persona

valorActividad:
    1.2: Poco o ningun ejercicio
    1.375: ejercicio ligero(1 a 3 dias por semana)
    1.55: ejercicio moderado (3 a 5 dias por semana)
    1.72: deportista (6-7 dias a la semana)
    1.9: atleta (entrenamiento mañana y tarde)
"""

    TMB = caloriasEnReposo(peso, altura, edad, valorGenero)
    TMBF = TMB * valorActividad
    return round(TMBF, 3)

    

    
    

