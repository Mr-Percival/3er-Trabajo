import tkinter as tk
import math


class Trabajador:
    def __init__(self, codigo, nombre, numero_horas, valor_hora, porcentaje_retefuente):
        self.codigo = codigo
        self.nombre = nombre
        self.numero_horas = numero_horas
        self.valor_hora = valor_hora
        self.porcentaje_retefuente = porcentaje_retefuente / 100
        self.salario_bruto = 0
        self.salario_neto = 0

    def calcular_salarios(self):
        self.salario_bruto = self.numero_horas * self.valor_hora
        self.salario_neto = self.salario_bruto - (self.salario_bruto * self.porcentaje_retefuente)

    def mostrar_informacion(self):
        return f'Código: {self.codigo}\nNombre: {self.nombre}\nSalario Bruto: {self.salario_bruto} pesos\nSalario Neto: {self.salario_neto} pesos'
class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado
        self.perimetro = 0
        self.altura = 0
        self.area = 0

    def calcular_propiedades(self):
        self.perimetro = self.lado * 3
        self.altura = (self.lado ** 2 - (self.lado / 2) ** 2) ** 0.5
        self.area = (self.lado * self.altura) / 2

    def mostrar_informacion(self):
        return (f'El triángulo tiene un lado de {self.lado} unidades\n'
                f'Un perímetro de {self.perimetro} unidades\n'
                f'Una altura de {self.altura} unidades\n'
                f'Un área de {self.area} unidades cuadradas')
class ComparadorValores:
    def __init__(self, valor_uno, valor_dos):
        self.valor_uno = valor_uno
        self.valor_dos = valor_dos
        self.resultado = ""

    def comparar(self):
        if self.valor_uno > self.valor_dos:
            self.resultado = f"El mayor valor es {self.valor_uno}"
        elif self.valor_uno == self.valor_dos:
            self.resultado = f"Los valores {self.valor_uno} y {self.valor_dos} son iguales"
        else:
            self.resultado = f"El mayor valor es {self.valor_dos}"

    def mostrar_resultado(self):
        return self.resultado
class Estudiante:
    def __init__(self, numero_inscripcion, nombre, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombre = nombre
        self.patrimonio = patrimonio
        self.estrato = estrato
        self.matricula = 50000

    def calcular_matricula(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            self.matricula += 0.03 * self.patrimonio

    def mostrar_informacion(self):
        return (f"El estudiante {self.nombre}\n"
                f"con numero de inscripción {self.numero_inscripcion}\n"
                f"deberá pagar {self.matricula} pesos de matricula")
class Empleado:
    def __init__(self, nombre, salario_por_hora, numero_horas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.numero_horas = numero_horas
        self.salario_mensual = 0

    def calcular_salario_mensual(self):
        self.salario_mensual = self.salario_por_hora * self.numero_horas

    def mostrar_informacion(self):
        if self.salario_mensual > 450000:
            return f"El nombre del empleado es {self.nombre} y su salario mensual es de {self.salario_mensual}"
        else:
            return f"El nombre del empleado es {self.nombre}"

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.soluciones = ""

    def calcular_soluciones(self):
        discriminante = self.b**2 - 4*self.a*self.c
        if discriminante > 0:
            x1 = (-self.b + math.sqrt(discriminante)) / (2*self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2*self.a)
            self.soluciones = f"Las soluciones son x1 = {x1} y x2 = {x2}"
        elif discriminante == 0:
            x = -self.b / (2*self.a)
            self.soluciones = f"La solución es x = {x}"
        else:
            self.soluciones = "No hay soluciones reales"

    def mostrar_soluciones(self):
        return self.soluciones
class AplicacionTrabajador:
    def __init__(self, master):
        self.master = master
        master.title("Formulario del Trabajador - Ejercicio 18 Capítulo 3")

        self.label_codigo = tk.Label(master, text="Código:")
        self.label_codigo.pack()
        self.entry_codigo = tk.Entry(master)
        self.entry_codigo.pack()

        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.label_numero_horas = tk.Label(master, text="Número de Horas:")
        self.label_numero_horas.pack()
        self.entry_numero_horas = tk.Entry(master)
        self.entry_numero_horas.pack()

        self.label_valor_hora = tk.Label(master, text="Valor por Hora:")
        self.label_valor_hora.pack()
        self.entry_valor_hora = tk.Entry(master)
        self.entry_valor_hora.pack()

        self.label_retefuente = tk.Label(master, text="Porcentaje de Retención en la Fuente:")
        self.label_retefuente.pack()
        self.entry_retefuente = tk.Entry(master)
        self.entry_retefuente.pack()

        self.boton_calcular = tk.Button(master, text="Calcular Salarios", command=self.calcular_salarios)
        self.boton_calcular.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def calcular_salarios(self):
        codigo = str(self.entry_codigo.get())
        nombre = self.entry_nombre.get()
        numero_horas = float(self.entry_numero_horas.get())
        valor_hora = float(self.entry_valor_hora.get())
        porcentaje_retefuente = float(self.entry_retefuente.get())

        trabajador = Trabajador(codigo, nombre, numero_horas, valor_hora, porcentaje_retefuente)
        trabajador.calcular_salarios()
        resultado = trabajador.mostrar_informacion()

        self.label_resultado.config(text=resultado)
class AplicacionTriangulo:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Triángulo Equilátero - Ejercicio 19 Capítulo 3")

        self.label_lado = tk.Label(master, text="Ingrese el lado del triángulo:")
        self.label_lado.pack()
        self.entry_lado = tk.Entry(master)
        self.entry_lado.pack()

        self.boton_calcular = tk.Button(master, text="Calcular Propiedades", command=self.calcular_propiedades)
        self.boton_calcular.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def calcular_propiedades(self):
        lado = float(self.entry_lado.get())
        triangulo = TrianguloEquilatero(lado)
        triangulo.calcular_propiedades()
        resultado = triangulo.mostrar_informacion()
        self.label_resultado.config(text=resultado)
class AplicacionComparador:
    def __init__(self, master):
        self.master = master
        master.title("Comparador de Valores - Ejercicio 7")

        self.label_valor_uno = tk.Label(master, text="Ingrese el 1er Valor:")
        self.label_valor_uno.pack()
        self.entry_valor_uno = tk.Entry(master)
        self.entry_valor_uno.pack()

        self.label_valor_dos = tk.Label(master, text="Ingrese el 2do Valor:")
        self.label_valor_dos.pack()
        self.entry_valor_dos = tk.Entry(master)
        self.entry_valor_dos.pack()

        self.boton_comparar = tk.Button(master, text="Comparar", command=self.comparar_valores)
        self.boton_comparar.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def comparar_valores(self):
        valor_uno = float(self.entry_valor_uno.get())
        valor_dos = float(self.entry_valor_dos.get())
        comparador = ComparadorValores(valor_uno, valor_dos)
        comparador.comparar()
        resultado = comparador.mostrar_resultado()
        self.label_resultado.config(text=resultado)
class AplicacionEstudiante:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo de Matrícula - Capítulo 4")

        self.label_numero_inscripcion = tk.Label(master, text="Número de Inscripción:")
        self.label_numero_inscripcion.pack()
        self.entry_numero_inscripcion = tk.Entry(master)
        self.entry_numero_inscripcion.pack()

        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.label_patrimonio = tk.Label(master, text="Patrimonio:")
        self.label_patrimonio.pack()
        self.entry_patrimonio = tk.Entry(master)
        self.entry_patrimonio.pack()

        self.label_estrato = tk.Label(master, text="Estrato Social:")
        self.label_estrato.pack()
        self.entry_estrato = tk.Entry(master)
        self.entry_estrato.pack()

        self.boton_calcular = tk.Button(master, text="Calcular Matrícula", command=self.calcular_matricula)
        self.boton_calcular.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def calcular_matricula(self):
        numero_inscripcion = self.entry_numero_inscripcion.get()
        nombre = self.entry_nombre.get()
        patrimonio = float(self.entry_patrimonio.get())
        estrato = int(self.entry_estrato.get())

        estudiante = Estudiante(numero_inscripcion, nombre, patrimonio, estrato)
        estudiante.calcular_matricula()
        resultado = estudiante.mostrar_informacion()
        self.label_resultado.config(text=resultado)
class AplicacionEmpleado:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Salario de Empleado - Capítulo 4")

        self.label_nombre = tk.Label(master, text="Nombre del Empleado:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.label_salario_por_hora = tk.Label(master, text="Salario por Hora:")
        self.label_salario_por_hora.pack()
        self.entry_salario_por_hora = tk.Entry(master)
        self.entry_salario_por_hora.pack()

        self.label_numero_horas = tk.Label(master, text="Número de Horas Trabajadas:")
        self.label_numero_horas.pack()
        self.entry_numero_horas = tk.Entry(master)
        self.entry_numero_horas.pack()

        self.boton_calcular = tk.Button(master, text="Calcular Salario", command=self.calcular_salario)
        self.boton_calcular.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def calcular_salario(self):
        nombre = self.entry_nombre.get()
        salario_por_hora = float(self.entry_salario_por_hora.get())
        numero_horas = float(self.entry_numero_horas.get())
        
        empleado = Empleado(nombre, salario_por_hora, numero_horas)
        empleado.calcular_salario_mensual()
        resultado = empleado.mostrar_informacion()
        self.label_resultado.config(text=resultado)
class AplicacionEcuacionCuadratica:
    def __init__(self, master):
        self.master = master
        master.title("Solucionador de Ecuaciones Cuadráticas - Capítulo 4")

        self.label_a = tk.Label(master, text="Valor de A:")
        self.label_a.pack()
        self.entry_a = tk.Entry(master)
        self.entry_a.pack()

        self.label_b = tk.Label(master, text="Valor de B:")
        self.label_b.pack()
        self.entry_b = tk.Entry(master)
        self.entry_b.pack()

        self.label_c = tk.Label(master, text="Valor de C:")
        self.label_c.pack()
        self.entry_c = tk.Entry(master)
        self.entry_c.pack()

        self.boton_calcular = tk.Button(master, text="Calcular Soluciones", command=self.calcular_soluciones)
        self.boton_calcular.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def calcular_soluciones(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        ecuacion = EcuacionCuadratica(a, b, c)
        ecuacion.calcular_soluciones()
        resultado = ecuacion.mostrar_soluciones()
        self.label_resultado.config(text=resultado)

def abrir_formulario_trabajador():
    nueva_ventana = tk.Toplevel(root)
    app = AplicacionTrabajador(nueva_ventana)

def abrir_formulario_triangulo():
    nueva_ventana = tk.Toplevel(root)
    app = AplicacionTriangulo(nueva_ventana)

def abrir_formulario_comparador():
    nueva_ventana = tk.Toplevel(root)
    app = AplicacionComparador(nueva_ventana)

def abrir_formulario_estudiante():
    nueva_ventana = tk.Toplevel(root)
    app = AplicacionEstudiante(nueva_ventana)

def abrir_formulario_empleado():
    nueva_ventana = tk.Toplevel(root)
    app = AplicacionEmpleado(nueva_ventana)

def abrir_formulario_ecuacion_cuadratica():
    nueva_ventana = tk.Toplevel(root)
    app = AplicacionEcuacionCuadratica(nueva_ventana)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Seleccione el Ejercicio a Ejecutar")
    root.geometry("400x500")

    label = tk.Label(root, text="Elija el ejercicio a ejecutar:", font=("Arial", 16))
    label.pack(pady=20)

    boton_ejercicio_trabajador = tk.Button(root, text="Ejercicio 18 Capítulo 3", font=("Arial", 14), command=abrir_formulario_trabajador)
    boton_ejercicio_trabajador.pack(pady=10)

    boton_ejercicio_triangulo = tk.Button(root, text="Ejercicio 19 Capítulo 3", font=("Arial", 14), command=abrir_formulario_triangulo)
    boton_ejercicio_triangulo.pack(pady=10)

    boton_ejercicio_comparador = tk.Button(root, text="Ejercicio 7 Capítulo 4", font=("Arial", 14), command=abrir_formulario_comparador)
    boton_ejercicio_comparador.pack(pady=10)

    boton_ejercicio_estudiante = tk.Button(root, text="Ejercicio 10 Capítulo 4", font=("Arial", 14), command=abrir_formulario_estudiante)
    boton_ejercicio_estudiante.pack(pady=10)

    boton_ejercicio_empleado = tk.Button(root, text="Ejercicio 22 Capítulo 4", font=("Arial", 14), command=abrir_formulario_empleado)
    boton_ejercicio_empleado.pack(pady=10)

    boton_ejercicio_ecuacion = tk.Button(root, text="Ejercicio 23 Capítulo 4", font=("Arial", 14), command=abrir_formulario_ecuacion_cuadratica)
    boton_ejercicio_ecuacion.pack(pady=10)

    root.mainloop()
