#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
from math import sqrt


 #bases numericas
    
def convertirdecimalabase(_numero, _base):  
    numeroconvertido = ""           
    _numero = int(_numero)           
    _base = int(_base)              
    while True:                     
        _residuo = _numero % _base   
        _numero -= _residuo         
        if _residuo >= 10:          
            _residuo += 55           
            numeroconvertido += str(chr(int(_residuo)))                   
        else:
            numeroconvertido += str(int(_residuo))
        _numero = _numero / _base   
        if _numero == 0:      
            break            
    numeroconvertido = numeroconvertido[::-1]                                               
    return numeroconvertido

def convertirbaseadecimal(_numero, _base):
    numeroconvertido = 0   
    _numero = str(_numero) 
    _base = int(_base)     
    _numero = _numero[::-1] 
    for i in range(0, len(_numero), 1):  
        if ord(_numero[i]) >= 65:  
            numeroconvertido += int(ord(_numero[i]) - 55) * pow(_base, i)  

        else:

            numeroconvertido += int(ord(_numero[i]) - 48) * pow(_base, i); # Convertimos numero asci en numero int
                                                                           # Multiplicamos numero por la base
                                                                           # elevada a la posicion, y lo suma a
                                                                           # la variable numeroconvertido
    return numeroconvertido


def numeros_primos():
    def pro_primos_1():
        primo = int(txtboxPrimo.get())
        numero = range(2, primo)
        contador = 0
        for n in numero:
            if primo % n == 0:
                contador += 1
        if contador > 0:
            messagebox.showinfo("Resultado", "EL NÚMERO NO ES PRIMO")
        else:
            messagebox.showinfo("Resultado", "EL NÚMERO ES PRIMO")

    ventanaPrimos = tk.Tk()
    ventanaPrimos.geometry('400x265')
    ventanaPrimos.title("Ventana Primos")
    ventanaPrimos.configure(background='#44FFED')
    lblCalculoPrimos = tk.Label(ventanaPrimos, text="CALCULADORA DE NÚMEROS PRIMOS", bg="#44FFED", fg="black")
    lblCalculoPrimos.pack(pady=40)
    lblDigiteNumero = tk.Label(ventanaPrimos, text="INGRESAR UN NÚMERO PARA CONOCER SI ES PRIMO O NO: ",
                               bg="#44FFED",
                               fg="black")
    lblDigiteNumero.pack(pady=15)
    txtboxPrimo = tk.Entry(ventanaPrimos)
    txtboxPrimo.pack()
    btnCalcular = tk.Button(ventanaPrimos, text="CONTINUAR", bg="azure", fg="black", command=pro_primos_1)
    btnCalcular.pack(pady=15)
    ventanaPrimos.mainloop()


def fibonacci():
    def f(n):
        return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))
    lista = []
    def solucionFibonacci():
        endNumber = int(txtboxFibonacci.get()) + 1
        n = 0
        cur = f(n)
        while cur <= endNumber:
            if 0 <= cur:
                enteros = int(cur)
                lista.append(enteros)
            n += 1
            cur = f(n)
        messagebox.showinfo("Resultado", lista)

    ventanaFibonacci = tk.Tk()
    ventanaFibonacci.geometry('450x290')
    ventanaFibonacci.title("Ventana Fibonacci")
    ventanaFibonacci.configure(background='#44FFED')
    lblCalculoFibonacci1 = tk.Label(ventanaFibonacci, text="CALCULADORA FIBONACCI", bg="#44FFED",
                                    fg="black")
    lblCalculoFibonacci1.pack(pady=40)
    lblDigiteNumero = tk.Label(ventanaFibonacci, text="INGRESAR NÚMERO FINAL DE LA SECUENCIA"
                                                      " (EL PROCESO INICIA DESDE 0): ",
                               bg="#44FFED", fg="black")
    lblDigiteNumero.pack(pady=15)
    txtboxFibonacci = tk.Entry(ventanaFibonacci)
    txtboxFibonacci.pack()
    btnCalcular = tk.Button(ventanaFibonacci, text="CONTINUAR", bg="azure", fg="black", command=solucionFibonacci)
    btnCalcular.pack(pady=15)
    ventanaFibonacci.mainloop()


def bases():
    def BaseaBase():
        numConv = int(txtboxNumeroConv.get())
        baseIni = int(txtboxBaseInicial.get())
        baseFinal = int(txtboxBaseFinal.get())
        paso1 = convertirbaseadecimal(numConv, baseIni)
        final = convertirdecimalabase(paso1, baseFinal)
        messagebox.showinfo("Resultado ", final)

    ventanaBaseaBase = tk.Tk()
    ventanaBaseaBase.geometry('300x400')
    ventanaBaseaBase.title("Ventana Bases")
    ventanaBaseaBase.configure(background='#44FFED')
    lblCalculoBaseaBase = tk.Label(ventanaBaseaBase, text="CALCULADORA DE BASES", bg="#44FFED", fg="black")
    lblCalculoBaseaBase.pack(pady=40)
    lblDigiteNumero1 = tk.Label(ventanaBaseaBase, text="BASE DEL NÚMERO ORIGINAL: ",
                                bg="#44FFED", fg="black")
    lblDigiteNumero1.pack(pady=15)
    txtboxBaseInicial = tk.Entry(ventanaBaseaBase)
    txtboxBaseInicial.pack()
    lblDigiteNumero2 = tk.Label(ventanaBaseaBase, text="NÚMERO QUE DESEA CONVERTIR: ", bg="#44FFED", fg="black")
    lblDigiteNumero2.pack(pady=15)
    txtboxNumeroConv = tk.Entry(ventanaBaseaBase)
    txtboxNumeroConv.pack()
    lblDigiteNumero3 = tk.Label(ventanaBaseaBase, text="BASE A LA QUE DESEA CONVERTIR: ",
                                bg="#44FFED", fg="black")
    lblDigiteNumero3.pack(pady=15)
    txtboxBaseFinal = tk.Entry(ventanaBaseaBase)
    txtboxBaseFinal.pack()
    btnCalcular = tk.Button(ventanaBaseaBase, text="CONTINUAR", bg="azure", fg="black", command=BaseaBase)
    btnCalcular.pack(pady=15)
    ventanaBaseaBase.mainloop()


def variaciones():
    def variacionV():
        n = int(elementosV.get())
        r = int(var.get())

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        if 0 <= r <= n:
            solucionV = (factorial(n) / factorial(n - r))
            messagebox.showinfo("Resultado", "Solución: " + str(solucionV))
        else:
            messagebox.showerror("Error", "DATOS INVALIDOS")

    def variacionR():
        n = int(elementosV.get())
        r = int(var.get())
        if n > 0 and r > 0:
            solucionR = (n ** r)
            messagebox.showinfo("Resultado", "Solución: " + str(solucionR))
        else:
            messagebox.showerror("Error", "DATOS INVALIDOS")

    ventanaVariaciones = tk.Tk()
    ventanaVariaciones.geometry('300x400')
    ventanaVariaciones.title("Ventana Variaciones")
    ventanaVariaciones.configure(background='#44FFED')
    lblCalculoVariacion = tk.Label(ventanaVariaciones, text="CALCULADORA DE VARIACIONES", bg="#44FFED", fg="black")
    lblCalculoVariacion.pack(pady=40)
    lblDigite_n = tk.Label(ventanaVariaciones, text="N-ELEMENTOS: ",
                           bg="#44FFED", fg="black")
    lblDigite_n.pack(pady=15)
    elementosV = tk.Entry(ventanaVariaciones)
    elementosV.pack()
    lblDigite_r = tk.Label(ventanaVariaciones, text="R-VARIACIONES: ",
                           bg="#44FFED", fg="black")
    lblDigite_r.pack(pady=15)
    var = tk.Entry(ventanaVariaciones)
    var.pack()
    btnCalcularV = tk.Button(ventanaVariaciones, text="OPERAR VARIACION", bg="azure", fg="black",
                             command=variacionV)
    btnCalcularV.pack(pady=15)
    btnCalcularVR = tk.Button(ventanaVariaciones, text="OPERAR VARIACION CON REPETICION", bg="azure", fg="black",
                              command=variacionR)
    btnCalcularVR.pack(pady=15)
    ventanaVariaciones.mainloop()


def permutaciones():
    def permutacionP():
        def permutacionPN():
            n = int(elementosPN.get())

            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n * factorial(n - 1)

            if n > 0:
                solucionP = factorial(n)
                messagebox.showinfo("Resultado", "PERMUTACIÓN: "
                                    + str(solucionP))
            else:
                messagebox.showerror("Error", "DATOS INVALIDOS")

        ventanaPermutacionesP = tk.Tk()
        ventanaPermutacionesP.geometry('320x300')
        ventanaPermutacionesP.title("Ventana Permutaciones 1")
        ventanaPermutacionesP.configure(background='#44FFED')
        lblCalculoPermutacionP = tk.Label(ventanaPermutacionesP, text="CALCULADORA DE PERMUTACIONES SIN REPETICIÓN", bg="#44FFED",
                                          fg="black")
        lblCalculoPermutacionP.pack(pady=40)
        lblDigite_P = tk.Label(ventanaPermutacionesP, text="N-ELEMENTOS: ",
                               bg="#44FFED", fg="black")
        lblDigite_P.pack(pady=15)
        elementosPN = tk.Entry(ventanaPermutacionesP)
        elementosPN.pack()
        btnCalcularPN = tk.Button(ventanaPermutacionesP, text="SIGUIENTE", bg="azure", fg="black",
                                  command=permutacionPN)
        btnCalcularPN.pack(pady=15)
        ventanaPermutacionesP.mainloop()

    def permutacionR():
        def permutacionPR():
            n = int(elementosPR.get())
            e1 = int(elementos1.get())
            e2 = int(elementos2.get())
            e3 = int(elementos3.get())
            e4 = int(elementos4.get())
            e5 = int(elementos5.get())

            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n * factorial(n - 1)

            if n > 0:
                solucionPR = ((factorial(n)) / (
                        factorial(e1) * factorial(e2) * factorial(e3) * factorial(e4) * factorial(e5)))
                messagebox.showinfo("Resultado", "PERMUTACIÓN: "
                                    + str(solucionPR))
            else:
                messagebox.showerror("Error", "DATOS INVALIDOS")

        ventanaPermutacionesPR = tk.Tk()
        ventanaPermutacionesPR.geometry('400x600')
        ventanaPermutacionesPR.title("Ventana Permutación 2")
        ventanaPermutacionesPR.configure(background='#44FFED')
        lblCalculoPermutacionPR = tk.Label(ventanaPermutacionesPR, text="CALCULADORA PERMUTACIONES CON REPETICIÓN",
                                           bg="#44FFED",
                                           fg="black")
        lblCalculoPermutacionPR.pack(pady=40)
        lblDigite_NPR = tk.Label(ventanaPermutacionesPR, text="N-ELEMENTOS: ",
                                 bg="#44FFED", fg="black")
        lblDigite_NPR.pack(pady=15)
        elementosPR = tk.Entry(ventanaPermutacionesPR)
        elementosPR.pack()
        lblDigite_E1 = tk.Label(ventanaPermutacionesPR, text="REPETICIÓN ELEMENTO 1: ",
                                bg="#44FFED", fg="black")
        lblDigite_E1.pack(pady=15)
        elementos1 = tk.Entry(ventanaPermutacionesPR)
        elementos1.pack()
        lblDigite_E2 = tk.Label(ventanaPermutacionesPR, text="REPETICIÓN ELEMENTO 2: ",
                                bg="#44FFED", fg="black")
        lblDigite_E2.pack(pady=15)
        elementos2 = tk.Entry(ventanaPermutacionesPR)
        elementos2.pack()
        lblDigite_E3 = tk.Label(ventanaPermutacionesPR, text="REPETICIÓN ELEMENTO 3: ",
                                bg="#44FFED", fg="black")
        lblDigite_E3.pack(pady=15)
        elementos3 = tk.Entry(ventanaPermutacionesPR)
        elementos3.pack()
        lblDigite_E4 = tk.Label(ventanaPermutacionesPR, text="REPETICIÓN ELEMENTO 4: ",
                                bg="#44FFED", fg="black")
        lblDigite_E4.pack(pady=15)
        elementos4 = tk.Entry(ventanaPermutacionesPR)
        elementos4.pack()
        lblDigite_E5 = tk.Label(ventanaPermutacionesPR, text="REPETICIÓN ELEMENTO 5: ",
                                bg="#44FFED", fg="black")
        lblDigite_E5.pack(pady=15)
        elementos5 = tk.Entry(ventanaPermutacionesPR)
        elementos5.pack()
        btnCalcularPR = tk.Button(ventanaPermutacionesPR, text="SIGUIENTE", bg="azure", fg="black",
                                  command=permutacionPR)
        btnCalcularPR.pack(pady=15)
        ventanaPermutacionesPR.mainloop()

    ventanaPermutaciones = tk.Tk()
    ventanaPermutaciones.geometry('300x320')
    ventanaPermutaciones.title("Ventana Permutaciones")
    ventanaPermutaciones.configure(background='#44FFED')
    lblCalculoPermutacion = tk.Label(ventanaPermutaciones, text="CALCULADORA DE PERMUTACIONES", bg="#44FFED", fg="black")
    lblCalculoPermutacion.pack(pady=40)
    lblDigite_P = tk.Label(ventanaPermutaciones, text="SELECCIONAR EL TIPO DE PERMUTACION A REALIZAR:",
                           bg="#44FFED", fg="black")
    lblDigite_P.pack(pady=15)
    btnCalcularP = tk.Button(ventanaPermutaciones, text="PERMUTACION", bg="azure", fg="black",
                             command=permutacionP)
    btnCalcularP.pack(pady=15)
    btnCalcularPR = tk.Button(ventanaPermutaciones, text="PERMUTACION CON REPETICION", bg="azure", fg="black",
                              command=permutacionR)
    btnCalcularPR.pack(pady=15)
    ventanaPermutaciones.mainloop()


def combinaciones():
    def combinacionC():
        n = int(elementosC.get())
        r = int(comb.get())

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        if 0 <= r <= n:
            solucionC = (factorial(n) / (factorial(r) * factorial(n - r)))
            messagebox.showinfo("Resultado", "COMBINACIÓN: " + str(solucionC))
        else:
            messagebox.showerror("Error", "DATOS INVALIDOS")

    def combinacionR():
        n = int(elementosC.get())
        r = int(comb.get())

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        if n > 0 and r > 0:
            solucionCR = (factorial(n + r - 1) / ((factorial(r)) * (factorial(n - 1))))
            messagebox.showinfo("Resultado", "COMBINACIÓN: "
                                + str(solucionCR))
        else:
            messagebox.showerror("Error", "DATOS INVALIDOS")

    ventanaCombinaciones = tk.Tk()
    ventanaCombinaciones.geometry('300x400')
    ventanaCombinaciones.title("Ventana Combinaciones")
    ventanaCombinaciones.configure(background='#44FFED')
    lblCalculoCombinacion = tk.Label(ventanaCombinaciones, text="CALCULADORA DE COMBINACIONES", bg="#44FFED", fg="black")
    lblCalculoCombinacion.pack(pady=40)
    lblDigite_n = tk.Label(ventanaCombinaciones, text="N-ELEMENTOS: ",
                           bg="#44FFED", fg="black")
    lblDigite_n.pack(pady=15)
    elementosC = tk.Entry(ventanaCombinaciones)
    elementosC.pack()
    lblDigite_r = tk.Label(ventanaCombinaciones, text="R-COMBINACIONES ",
                           bg="#44FFED", fg="black")
    lblDigite_r.pack(pady=15)
    comb = tk.Entry(ventanaCombinaciones)
    comb.pack()
    btnCalcularC = tk.Button(ventanaCombinaciones, text="OPERAR COMBINACIÓN", bg="azure", fg="black",
                             command=combinacionC)
    btnCalcularC.pack(pady=15)
    btnCalcularCR = tk.Button(ventanaCombinaciones, text="OPERAR COMBINACIÓN CON REPETICION", bg="azure", fg="black",
                              command=combinacionR)
    btnCalcularCR.pack(pady=15)
    ventanaCombinaciones.mainloop()


ventanaOpciones = tk.Tk()
ventanaOpciones.geometry('300x450')
ventanaOpciones.title("Ventana de Main")
ventanaOpciones.configure(background='#44FFED')
lblOpciones = tk.Label(ventanaOpciones, text="ELIGE LA OPCIÓN QUE DESEES OPERAR", bg="#44FFED", fg="black")
lblOpciones.pack(pady=30)
btnCalcular1 = tk.Button(ventanaOpciones, text="PRIMOS", bg="azure", fg="black", command=numeros_primos)
btnCalcular1.pack(pady=15)
btnCalcular2 = tk.Button(ventanaOpciones, text="FIBONACCI", bg="azure", fg="black", command=fibonacci)
btnCalcular2.pack(pady=15)
btnCalcular3 = tk.Button(ventanaOpciones, text="BASES", bg="azure", fg="black", command=bases)
btnCalcular3.pack(pady=15)
btnCalcular4 = tk.Button(ventanaOpciones, text="VARIACIONES", bg="azure", fg="black", command=variaciones)
btnCalcular4.pack(pady=15)
btnCalcular5 = tk.Button(ventanaOpciones, text="PERMUTACIONES", bg="azure", fg="black", command=permutaciones)
btnCalcular5.pack(pady=15)
btnCalcular6 = tk.Button(ventanaOpciones, text="COMBINACIONES", bg="azure", fg="black", command=combinaciones)
btnCalcular6.pack(pady=15)
ventanaOpciones.mainloop()


# In[ ]:




