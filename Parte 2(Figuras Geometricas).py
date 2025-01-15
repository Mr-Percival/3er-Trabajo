import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

class TrianguloRectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def tipo_triangulo(self):
        a = self.base
        b = self.altura
        c = self.hipotenusa()
        
        if a == b == c:
            return "Equilátero"
        elif a == b or b == c or a == c:
            return "Isósceles"
        else:
            return "Escaleno"

def calcular():
    figura = seleccion.get()
    if figura == "Círculo":
        radio = float(entrada1.get())
        circulo = Circulo(radio)
        area = circulo.area()
        perimetro = circulo.perimetro()
        messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimetro}")
    elif figura == "Rectángulo":
        base = float(entrada1.get())
        altura = float(entrada2.get())
        rectangulo = Rectangulo(base, altura)
        area = rectangulo.area()
        perimetro = rectangulo.perimetro()
        messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimetro}")
    elif figura == "Cuadrado":
        lado = float(entrada1.get())
        cuadrado = Cuadrado(lado)
        area = cuadrado.area()
        perimetro = cuadrado.perimetro()
        messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimetro}")
    elif figura == "Triángulo Rectángulo":
        base = float(entrada1.get())
        altura = float(entrada2.get())
        triangulo = TrianguloRectangulo(base, altura)
        area = triangulo.area()
        perimetro = triangulo.perimetro()
        hipotenusa = triangulo.hipotenusa()
        tipo = triangulo.tipo_triangulo()
        messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimetro}\nHipotenusa: {hipotenusa}\nTipo: {tipo}")

def mostrar_opciones():
    global seleccion, entrada1, entrada2
    ventana_opciones = tk.Tk()
    ventana_opciones.title("Seleccionar Figura Geométrica")

    tk.Label(ventana_opciones, text="Seleccione una figura geométrica:", font=("Arial", 14)).pack()

    seleccion = tk.StringVar(ventana_opciones)
    seleccion.set("Círculo") 

    opciones = ["Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo"]
    menu = tk.OptionMenu(ventana_opciones, seleccion, *opciones)
    menu.config(font=("Arial", 14))
    menu.pack()

    tk.Button(ventana_opciones, text="Aceptar", font=("Arial", 14), command=lambda: [ventana_opciones.destroy(), mostrar_inputs()]).pack()

    ventana_opciones.mainloop()

def mostrar_inputs():
    global entrada1, entrada2
    ventana = tk.Tk()
    ventana.title("Figuras Geométricas")

    figura = seleccion.get()
    if figura == "Círculo" or figura == "Cuadrado":
        tk.Label(ventana, text="Valor (Lado):", font=("Arial", 14)).pack()
        entrada1 = tk.Entry(ventana, font=("Arial", 14))
        entrada1.pack()
        entrada2 = tk.Entry(ventana, font=("Arial", 14))
        entrada2.pack_forget() # No se necesita la segunda entrada

    else:
        tk.Label(ventana, text="Valor 1 (Base):", font=("Arial", 14)).pack()
        entrada1 = tk.Entry(ventana, font=("Arial", 14))
        entrada1.pack()

        tk.Label(ventana, text="Valor 2 (Altura):", font=("Arial", 14)).pack()
        entrada2 = tk.Entry(ventana, font=("Arial", 14))
        entrada2.pack()

    tk.Button(ventana, text="Calcular", font=("Arial", 14), command=calcular).pack()
    
    ventana.mainloop()

mostrar_opciones()
