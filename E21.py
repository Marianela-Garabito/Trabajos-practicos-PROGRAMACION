import tkinter as tk
from tkinter import ttk


def convertir():
    try:
        x = float(entrada.get())
        Conversion = conversion.get()

        if Conversion == "m a km":
            r = x / 1000

        elif Conversion == "m a millas":
            r = x * 0.000621

        elif Conversion == "cm a pulg":
            r = x * 0.3937

        elif Conversion == "m a pies":
            r = x * 3.2808

        # Temperatura
        elif Conversion == "Celsius a Fahrenheit":
            r = x * 9 / 5 + 32

        elif Conversion == "Celsius a Kelvin":
            r = x + 273.15

        elif Conversion == "Fahrenheit a Kelvin":
            r = (x - 32) * 5 / 9 + 273.15

        # Masa
        elif Conversion == "kg a lb":
            r = x * 2.2046

        elif Conversion == "gr a onzas":
            r = x * 0.03527

        elif Conversion == "tn a kg":
            r = x * 1000

        # Velocidad
        elif Conversion == "km/h a mph":
            r = x * 0.6213

        elif Conversion == "km/h a m/s":
            r = x / 3.6

        elif Conversion == "km/h a nudos":
            r = x * 0.54

        # Volumen
        elif Conversion == "litros a galones":
            r = x * 0.2642

        elif Conversion == "litros a pies cubicos":
            r = x * 0.0353

        # Monedas
        elif Conversion == "pesos a dolares":
            r = x / 1450

        elif Conversion == "pesos a reales":
            r = x / 270

        elif Conversion == "pesos a euros":
            r = x / 1700

        # Informática
        elif Conversion == "B a KB":
            r = x / 1024

        elif Conversion == "KB a MB":
            r = x / 1024

        elif Conversion == "MB a GB":
            r = x / 1024

        resultado.config(text=f"Resultado: {round(r, 4)}")

    except ValueError:
        resultado.config(text="Ingrese un número válido")


def cambiar_categoria(*args):
    datos = {
        "Longitud": [
            "m a km",
            "m a millas",
            "cm a pulg",
            "m a pies"
        ],

        "Temperatura": [
            "Celsius a Fahrenheit",
            "Celsius a Kelvin",
            "Fahrenheit a Kelvin"
        ],

        "Masa": [
            "kg a lb",
            "gr a onzas",
            "tn a kg"
        ],

        "Velocidad": [
            "km/h a mph",
            "km/h a m/s",
            "km/h a nudos"
        ],

        "Volumen": [
            "litros a galones",
            "litros a pies cubicos"
        ],

        "Monedas": [
            "pesos a dolares",
            "pesos a reales",
            "pesos a euros"
        ],

        "Informatica": [
            "B a KB",
            "KB a MB",
            "MB a GB"
        ]
    }

    conversion["values"] = datos[categoria.get()]
    conversion.current(0)


ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("400x500")


# Título
tk.Label(
    ventana,
    text="CONVERSOR DE UNIDADES",
    font=("Times New Roman", 20, "bold")
).pack(pady=20)


# Línea
linea = tk.Frame(
    ventana,
    height=2,
    bg="black",
    width=325
)

linea.pack(pady=(1, 10))


categoria = tk.StringVar(value="Longitud")

tk.Label(
    ventana,
    text="Categoría:",
    font=("Arial", 14, "bold")
).pack(pady=10)


tk.OptionMenu(
    ventana,
    categoria,
    "Longitud",
    "Temperatura",
    "Masa",
    "Velocidad",
    "Volumen",
    "Monedas",
    "Informatica"
).pack(pady=5)


categoria.trace_add("write", cambiar_categoria)


tk.Label(
    ventana,
    text="Conversión:",
    font=("Arial", 14, "bold")
).pack(pady=10)


conversion = ttk.Combobox(
    ventana,
    state="readonly"
)

conversion["values"] = [
    "m a km",
    "m a millas",
    "cm a pulg",
    "m a pies"
]

conversion.current(0)
conversion.pack(pady=5)


tk.Label(
    ventana,
    text="Valor:",
    font=("Arial", 14, "bold")
).pack(pady=10)


entrada = tk.Entry(
    ventana,
    font=("Arial", 12),
    justify="center"
)

entrada.pack(pady=5)


boton = tk.Button(
    ventana,
    text="Convertir",
    width=12,
    height=1,
    font=("Arial", 12, "bold"),
    command=convertir
)

boton.pack(pady=(5, 5))

resultado = tk.Label(
    ventana,
    text="Resultado",
    font=("Arial", 14, "bold")
)

resultado.pack(pady=10)


ventana.mainloop()
