import tkinter as tk


def cesar():
    mensaje = entrada.get()
    desplazamiento = int(numero.get())

    resultado = ""

    for letra in mensaje:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nueva = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado += nueva
        else:
            resultado += letra

    salida.delete(0, tk.END)
    salida.insert(0, resultado)


def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Cifrado César")
    ventana.geometry("400x300")
    ventana.config(bg="#DCEEFF")

    tk.Label(
        ventana,
        text="Cifrado César",
        font=("Arial", 20, "bold"),
        bg="#DCEEFF"
    ).pack(pady=15)

    tk.Label(
        ventana,
        text="Mensaje:",
        bg="#DCEEFF"
    ).pack()

    global entrada
    entrada = tk.Entry(ventana, width=40)
    entrada.pack(pady=5)

    tk.Label(
        ventana,
        text="Desplazamiento:",
        bg="#DCEEFF"
    ).pack()

    global numero
    numero = tk.Entry(ventana, width=10)
    numero.pack(pady=5)

    boton = tk.Button(
        ventana,
        text="Cifrar / Descifrar",
        command=cesar,
        bg="#3498DB",
        fg="white"
    )
    boton.pack(pady=15)

    tk.Label(
        ventana,
        text="Resultado:",
        bg="#DCEEFF"
    ).pack()

    global salida
    salida = tk.Entry(ventana, width=40)
    salida.pack(pady=5)

    ventana.mainloop()


crear_ventana()