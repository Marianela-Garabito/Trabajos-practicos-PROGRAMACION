import tkinter as tk
import random
    
# Objeto de clase tkinter/Tk
secreto= random.randint(1, 20)
vidas =6
app = tk.Tk()
Entrada = tk.StringVar(app)
VidasSV= tk.StringVar(app)
resultado= tk.StringVar(app)# Consola

def intentar():
    global vidas
    if(vidas <= 0):
        resultado.set("perdiste")
        vidas= vidas - 1
        return
    numero_ingresado = int(Entrada.get())
    
    if(numero_ingresado < secreto):
        resultado.set("el numero ingresado es muy bajo")
        vidas= vidas - 1
    if(numero_ingresado > secreto):
        resultado.set("el numero ingresado es muy alto")
        vidas= vidas - 1
        
    if(numero_ingresado == secreto):
        resultado.set("felicidades, ganaste")
    VidasSV.set("vidas: "+ str(vidas))
    
def jugar():
    inicio.pack_forget()# Deja de mostrar la pantalla de inicio
    juego.pack(fill="both",expand=True)# Muestra la pantalla de juego
    
def salir():
    app.destroy()# Cierra la ventana por completo

# VENTANA
# Tamaño = ancho x alto
app.geometry("400x500")
# Color de fondo
app.configure(background = "#E67E28")
# Titulo
tk.Wm.wm_title(app,"adivina el numero")

# PANTALLA DE INICIO
inicio=tk.Frame(app, bg="#E67E28")

tk.Label(
    inicio,
    text="¿Desea jugar?",
    font=("Arial",20),
    bg="#E67E28",
    fg="#6E2C00"
).pack(pady=30)

tk.Button(
    inicio,
    text="Sí",
    font=("Arial",14),
    command=jugar
).pack(pady=10)

tk.Button(
    inicio,
    text="No",
    font=("Arial",14),
    command=salir
).pack(pady=10)

# JUEGO
# Mostrar texto en pantalla
juego=tk.Frame(app, bg="#E67E28")# Ingresar una seccion dentro de la ventana 

tk.Label(
    juego,
    text= "Adivina el numero entre 1 y 20",
    font=("Arial",20),
    bg= "#E67E28",# Background
    fg= "#6E2C00",# Foreground
    justify= "center"
).pack(
    expand = "true"
    )

# Mostrar texto en pantalla
tk.Label(
    juego,
    text= "vidas: ",
    font=("Arial",15),
    bg= "#FFD54F",
    fg= "#6E2C00",
    justify= "center",
    textvariable=VidasSV
).pack(
    expand = "true"
    )

# Ingresar texto
tk.Entry(
    juego,
    font=("Arial",15),
    bg= "#F57C00",
    fg= "#6E2C00",
    justify= "center",
    textvariable= Entrada
).pack(
    #fill = tk.BOTH,
    expand = "True"
    )

# Crear el boton
tk.Button(juego,
    # Texto
    text= "adivina",
    # Color de fondo
    bg="grey",
    # Color de texto
    fg="black",
    # Fuente del texto
    font=("Arial",14),
    command=intentar
    # Mostrar texto
    ).pack(expand = "True")

# Mostrar texto en pantalla
tk.Label(
    juego,
    #textvariable= ,
    textvariable=resultado,
    font=("Arial",15),
    bg= "#FFD54F",
    fg= "#6E2C00",
    justify= "center"
).pack(
    expand = "true"
    )

inicio.pack(fill="both", expand=True)

app.mainloop()