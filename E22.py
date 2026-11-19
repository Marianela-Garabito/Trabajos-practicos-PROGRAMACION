import tkinter as tk
from tkinter import messagebox

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def procesar(mensaje, clave, descifrar=False):
    clave = clave.upper().replace(" ", "")

    if not clave or any(letra not in ALFABETO for letra in clave):
        messagebox.showerror("Error", "Ingrese una clave válida.")
        return None

    resultado = ""
    posicion = 0

    for caracter in mensaje:
        letra = caracter.upper()

        if letra in ALFABETO:
            desplazamiento = ALFABETO.index(clave[posicion % len(clave)])

            if descifrar:
                desplazamiento = -desplazamiento

            nueva_posicion = (
                ALFABETO.index(letra) + desplazamiento
            ) % len(ALFABETO)

            nueva_letra = ALFABETO[nueva_posicion]

            if caracter.islower():
                nueva_letra = nueva_letra.lower()

            resultado += nueva_letra
            posicion += 1
        else:
            resultado += caracter

    return resultado


def cifrar():
    mensaje = entrada.get("1.0", tk.END).rstrip("\n")
    clave = clave_entrada.get()

    resultado = procesar(mensaje, clave)

    if resultado is not None:
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, resultado)


def descifrar():
    mensaje = entrada.get("1.0", tk.END).rstrip("\n")
    clave = clave_entrada.get()

    resultado = procesar(mensaje, clave, True)

    if resultado is not None:
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, resultado)


def limpiar():
    entrada.delete("1.0", tk.END)
    salida.delete("1.0", tk.END)
    clave_entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Cifrado Vigenère")
ventana.geometry("600x520")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="CIFRADO VIGENÈRE",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

tk.Label(
    ventana,
    text="Mensaje:",
    font=("Arial", 11, "bold")
).pack()

entrada = tk.Text(ventana, height=7, width=65)
entrada.pack(pady=5)

tk.Label(
    ventana,
    text="Clave:",
    font=("Arial", 11, "bold")
).pack(pady=5)

clave_entrada = tk.Entry(ventana, width=35, font=("Arial", 11))
clave_entrada.pack(pady=5)

botones = tk.Frame(ventana)
botones.pack(pady=12)

tk.Button(
    botones,
    text="Cifrar",
    width=13,
    command=cifrar
).grid(row=0, column=0, padx=5)

tk.Button(
    botones,
    text="Descifrar",
    width=13,
    command=descifrar
).grid(row=0, column=1, padx=5)

tk.Button(
    botones,
    text="Limpiar",
    width=13,
    command=limpiar
).grid(row=0, column=2, padx=5)

tk.Label(
    ventana,
    text="Resultado:",
    font=("Arial", 11, "bold")
).pack(pady=5)

salida = tk.Text(ventana, height=7, width=65)
salida.pack(pady=5)

ventana.mainloop()
