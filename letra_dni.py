from tkinter import *

raiz = Tk()
raiz.title("Calculadora Letra Dni")
raiz.geometry('300x100+350+150')


miFrame = Frame(raiz)

miFrame.pack()

datoPantalla = StringVar()

# Defino la interfaz de la pantalla

etiqueta = Label(miFrame, text="DNI :")
etiqueta.grid(row=0, column=0)

pantalla = Entry(miFrame, textvariable=datoPantalla)

pantalla.grid(row=0, column=1, padx=10, pady=10)

pantalla.config(background="black", fg="#03f943", justify="left")

bntCalcular = Button(miFrame, text="Calcular", width=6, command=lambda:calculaLetra())
bntCalcular.grid(row=0, column=2)

def calculaLetra():

    listaLetras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    try:
        dni = int(datoPantalla.get())
        resultado = dni % 23

        datoPantalla.set(datoPantalla.get() + '-' + listaLetras[resultado])

    except TypeError:

        print("Error Dato No valido")

    except:

        print("Error inesperado")


raiz.mainloop()