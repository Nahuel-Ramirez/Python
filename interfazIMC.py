from tkinter import * 
import logicaIndices as ind
import getpass

root = Tk()
root.title("Indice de Masa Corporal")
root.geometry("550x500")
root.config(bg ="linen")
root.resizable(0,0)

# Variables
peso = IntVar()
altura = DoubleVar()
resultado = StringVar()

#Logica
peso.set("")
altura.set("")

def ejecIMC()->float:
    IMC = ind.calcularIMC(peso.get(), altura.get())
    return resultado.set(IMC)

#Etiquetas 

#Etiqueta para el saludo de bienvenida.
etiquetaSaludo = Label(root, text="Bienvenido/a, a continuacion, se le pedira peso(kg) y altura(m) para calcular su indice de masa corporal.", bd=5, bg="bisque", font="curier3", wraplength=500)
etiquetaSaludo.place(x=30, y=20)


#Etiqueta para el peso
etiquetaPeso = Label(root, text="Ingrese su peso(kg)", bd=5, bg="antique white", border=8, font="curier3")
etiquetaPeso.place(x=40,y=80)

ingresoPeso = Entry(bd=5, border=5, width=10, textvariable=peso)
ingresoPeso.place(x=198,y=83)


#Etiqueta para la altura
etiquetaAltura = Label(root, text="Ingrese su altura(m)", bd=5, bg="antique white", border=8, font="curier3")
etiquetaAltura.place(x=40,y=160)

ingresoAltura = Entry(bd=5, border=5, width=10, textvariable=altura)
ingresoAltura.place(x=198,y=166)


#Boton que desarrolla la logica del programa
botonOperacion = Button(text= "Realizar Operacion", bd=5, bg="antique white", font="curier3", relief="groove", activebackground="linen", command=ejecIMC)
botonOperacion.place(x=300, y=124)


#Etiqueta Resultado
etiquetaResultado = Label(root, text="Tu indice de masa corporal es de",bd=5, bg="antique white", border=8, font="curier3", wraplength=500)
etiquetaResultado.place(x=150, y=245)

campoResultado =Entry(bd=5, border=5, textvariable=resultado, state="disabled")
campoResultado.place(x=200, y=300)








root.mainloop()