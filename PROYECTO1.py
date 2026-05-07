import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
import os
cred = credentials.Certificate(r"D:\Javier4B\contraseñabasededatos.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()


USUARIO = "javier"

datos_cotizacion = {}
facturas = [
    {"numero": 1, "fecha": "01/01/2025", "monto": 450},
    {"numero": 2, "fecha": "05/01/2025", "monto": 600},
    {"numero": 3, "fecha": "10/01/2025", "monto": 300},
    {"numero": 4, "fecha": "15/01/2025", "monto": 900},
    {"numero": 5, "fecha": "20/01/2025", "monto": 750},
]

def cargar_imagen(ruta, tamaño):
    img = Image.open(ruta)
    img = img.resize(tamaño)
    return ImageTk.PhotoImage(img)

def crear_marco_superior(ventana):
    frame_superior = tk.Frame(ventana, bg="black")
    frame_superior.grid(row=0, column=0, columnspan=2, pady=10)

    img_logo = cargar_imagen("C:/Users/alema/Downloads/imagenesproyecto/LOGO.jpeg", (100, 100))
    label_img = tk.Label(frame_superior, image=img_logo, bg="black")
    label_img.image = img_logo
    label_img.grid(row=0, column=0, rowspan=2, padx=20)
  

    label_titulo = tk.Label(frame_superior, text="ZONA SPORT FIT GYM", font=("Impact", 20), bg="red")
    label_titulo.grid(row=0, column=1, sticky="w")

    label_subtitulo = tk.Label(frame_superior, text="SALUD Y FIGURA", font=("Impact", 14), bg="red")
    label_subtitulo.grid(row=1, column=1, sticky="w")

def crear_imagenes_inferiores(ventana):
    img_izq = cargar_imagen("C:/Users/alema/Downloads/imagenesproyecto/COPY.webp", (90, 90))
    label_izq = tk.Label(ventana, image=img_izq, bg="black")
    label_izq.image = img_izq
    label_izq.place(x=0, rely=1.0, anchor="sw")

    img_der = cargar_imagen("C:/Users/alema/Downloads/imagenesproyecto/LOGOS.png", (100, 60))
    label_der = tk.Label(ventana, image=img_der, bg="black")
    label_der.image = img_der
    label_der.place(relx=1.0, rely=1.0, anchor="se")

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def crear_botones(ventana, botones_habilitados):
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=2, column=0, columnspan=2)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    style = ttk.Style()
    style.theme_use("default")

    style.configure("BotonNegro.TButton",
                background="black",
                foreground="white",
                font=("Arial", 10, "bold"))

    style.map("BotonNegro.TButton",
                background=[("active", "#333333")])

    b1 = ttk.Button(frame_botones, text="Login", style="BotonNegro.TButton", command=lambda: mostrar_ventana1(ventana))
    b2 = ttk.Button(frame_botones, text="Inicio", style="BotonNegro.TButton", command=lambda: mostrar_ventana2(ventana))
    b3 = ttk.Button(frame_botones, text="Comentarios", style="BotonNegro.TButton", command=lambda: mostrar_ventana3(ventana))
    b4 = ttk.Button(frame_botones, text="Catalogo", style="BotonNegro.TButton", command=lambda: mostrar_ventana4(ventana))
    b5 = ttk.Button(frame_botones, text="Cotizacion", style="BotonNegro.TButton", command=lambda: mostrar_ventana5(ventana))
    b6 = ttk.Button(frame_botones, text="Factura", style="BotonNegro.TButton", command=lambda: mostrar_ventana6(ventana))
    b7 = ttk.Button(frame_botones, text="Registro", style="BotonNegro.TButton", command=lambda: mostrar_ventana7(ventana))
    b8 = ttk.Button(frame_botones, text="Perfil", style="BotonNegro.TButton", command=lambda: mostrar_ventana8(ventana))

    b1.grid(row=0, column=0, padx=0)
    b2.grid(row=0, column=1, padx=0)
    b3.grid(row=0, column=2, padx=0)
    b4.grid(row=0, column=3, padx=0)
    b5.grid(row=0, column=4, padx=0)
    b6.grid(row=0, column=5, padx=0)
    b7.grid(row=0, column=6, padx=0)
    b8.grid(row=0, column=7, padx=0)

    for i, habilitado in enumerate(botones_habilitados):
        if not habilitado:
            frame_botones.grid_slaves(row=0, column=i)[0].config(state="disabled")

    return [b1, b2, b3, b4, b5, b6, b7, b8]

def mostrar_ventana1(ventana=None):
    if ventana is None:
        ventana = tk.Tk()
        ventana.title("Ventana 1 - Login")
        ventana.geometry("750x750")
        ventana.configure(bg="black")
        global CONTRASENA
        CONTRASENA = tk.StringVar(value="123")
    else:
        limpiar_ventana(ventana)

    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)

    botones = crear_botones(ventana, [True, False, False, False, False, False, False, False])
    frame_login = tk.Frame(ventana, bg="RED")
    frame_login.grid(row=3, column=0, columnspan=2, pady=20)

    tk.Label(frame_login, text="Usuario:", bg="red", font=("Impact" , 15)).grid(row=0, column=0, padx=5, pady=5)
    usuario_entry = ttk.Entry(frame_login)
    usuario_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_login, text="Contraseña:", bg="red", font=("Impact" , 15)).grid(row=1, column=0, padx=5, pady=5)
    contrasena_entry = ttk.Entry(frame_login, show="*")
    contrasena_entry.grid(row=1, column=1, padx=5, pady=5)

    def validar_login():
        usuario_input = usuario_entry.get().strip()
        contrasena_input = contrasena_entry.get().strip()

        doc_ref = db.collection("CONTRASEÑA").document("contraseña")
        doc = doc_ref.get()

        if not doc.exists:
            messagebox.showerror("Error", "No existe el documento en la base de datos")
            return

        data = doc.to_dict()

        usuario_db = data.get("usuario")
        contrasena_db = data.get("contraseña")

        if usuario_input == usuario_db and contrasena_input == contrasena_db:
            messagebox.showinfo("Éxito", "Login correcto")
            for b in botones:
                b.config(state="normal")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(frame_login, text="Iniciar sesión", command=validar_login, bg="YELLOW").grid(row=2, column=0, columnspan=2, pady=10)

    label_olvido = tk.Label(frame_login, text="¿Olvidaste tu contraseña?", font=("Impact", 15), bg="red")
    label_olvido.grid(row=3, column=0, columnspan=2, pady=5)

    def recuperar_contrasena():
        messagebox.showinfo("Recuperar contraseña", "Por favor contacta al administrador para restablecer tu contraseña al numero: 2213753278")
    tk.Button(frame_login, text="Recuperar", command=recuperar_contrasena, bg="YELLOW").grid(row=4, column=0, columnspan=2, pady=5)
    ventana.mainloop()

def mostrar_ventana2(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True, True, True, True, True, True, True, True])

    tk.Label(ventana, text="Inicio", font=("Impact", 20), bg="black", fg="white").grid(row=4, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Visión:", font=("Impact", 12), bg="black", fg="white").grid(row=5, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Ayudar a mas personas a mejorar su fisico y lograr mejorar tanto su salud como su bolsillo", font=("Impact", 12), bg="black", fg="white").grid(row=6, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Misión:", font=("Impact", 12), bg="black", fg="white").grid(row=7, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Crear en ti una fuerza tanto mental como fisica para que puedas lograr todos tus objetivos", font=("Impact", 12), bg="black", fg="white").grid(row=8, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Ubicación: Calle tepetitlan, Lomas del sur, Puebla", font=("Impact", 12), bg="black", fg="white").grid(row=9, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Logros de la empresa:", font=("Impact", 12), bg="black", fg="white").grid(row=10, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Ser de los mejores gimnasios de la zona", font=("Impact", 12), bg="black", fg="white").grid(row=11, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Buenas criticas hacia el gimnasio", font=("Impact", 12), bg="black", fg="white").grid(row=12, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Contar con una buena cantidad de equipos", font=("Impact", 12), bg="black", fg="white").grid(row=13, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Evitar un gasto fuerte al bolsillo de los clientes", font=("Impact", 12), bg="black", fg="white").grid(row=14, column=0, columnspan=3, padx=50, pady=10)


def mostrar_ventana3(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True]*8)

    frame = tk.Frame(ventana, bg="black")
    frame.grid(row=3, column=0, columnspan=2, pady=20)

    tk.Label(frame, text="Formulario de Contacto",
             font=("Impact", 12),
             bg="black", fg="white").grid(row=0, column=0, columnspan=2, pady=10)


    tk.Label(frame, text="Comentario:",
             font=("Impact", 12),
             bg="black", fg="white").grid(row=1, column=0, sticky="w")

    caja_texto = tk.Text(frame, width=50, height=8,
                         font=("Impact", 12))
    caja_texto.grid(row=2, column=0, columnspan=2, pady=10)

    
    ruta_imagen = {"ruta": ""}

    def seleccionar_imagen():
        archivo = filedialog.askopenfilename(
            filetypes=[("Imagenes", "*.png *.jpg *.jpeg *.webp")]
        )
        if archivo:
            ruta_imagen["ruta"] = archivo
            label_imagen.config(text="Imagen seleccionada ✔")
            img = Image.open(archivo)
            img = img.resize((150, 150))  # tamaño preview
            img_tk = ImageTk.PhotoImage(img)
            label_preview.config(image=img_tk)
            label_preview.image = img_tk 

    tk.Button(frame, text="Subir imagen",
              font=("Impact", 12),
              bg="yellow",
              command=seleccionar_imagen).grid(row=3, column=0, pady=10)

    label_imagen = tk.Label(frame, text="Ninguna imagen",
                            font=("Impact", 12),
                            bg="black", fg="white")
    label_imagen.grid(row=3, column=1)

    # 🚀 Guardar en Firebase
    def enviar():
        comentario = caja_texto.get("1.0", "end").strip()

        if comentario == "":
            messagebox.showerror("Error", "Escribe un comentario")
            return

        db.collection("COMENTARIOS").add({
            "comentario": comentario,
            "imagen": ruta_imagen["ruta"],
            "fecha": datetime.now()
        })

        messagebox.showinfo("Éxito", "Comentario enviado")

        caja_texto.delete("1.0", "end")
        label_imagen.config(text="Ninguna imagen")
        ruta_imagen["ruta"] = ""

    tk.Button(frame, text="Enviar",
              font=("Impact", 12),
              bg="red", fg="white",
              command=enviar).grid(row=4, column=0, columnspan=2, pady=10)
    label_preview = tk.Label(frame, bg="black")
    label_preview.grid(row=5, column=0, columnspan=2, pady=10)


    

def mostrar_ventana4(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True, True, True, True, True, True, True, True])
    tk.Label(ventana, text="Precios por pieza:", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Aceite para pestañas").grid(row=4, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Prosa").grid(row=5, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$60").grid(row=6, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Labial Mate").grid(row=7, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Italia deluxe").grid(row=8, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$48").grid(row=9, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Polvo traslucido").grid(row=10, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Pink up").grid(row=11, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$110").grid(row=12, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Gloss").grid(row=13, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Italia deluxe").grid(row=14, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$60").grid(row=15, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Rizador de pestañas").grid(row=4, column=1, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Princessa").grid(row=5, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$36").grid(row=6, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Delineador de ojos").grid(row=7, column=1, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Prosa").grid(row=8, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$37").grid(row=9, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Labial").grid(row=10, column=1, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Pink up").grid(row=11, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$49").grid(row=12, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="-Nombre:Polvo matificante").grid(row=13, column=1, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Marca:Pink up").grid(row=14, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="Precio:$115").grid(row=15, column=1, columnspan=3, padx=50, pady=1)
    tk.Label(ventana, text="Promociones:").grid(row=16, column=0, columnspan=2, padx=50, pady=1)
    tk.Label(ventana, text="Labial 2X1").grid(row=17, column=0, columnspan=2, padx=50, pady=1) 
    tk.Label(ventana, text="Gloss descuento del 10%").grid(row=18, column=0, columnspan=2, padx=50, pady=1)

def mostrar_ventana5(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True, True, True, True, True, True, True, True])
    tk.Label(ventana, text="Ingrese cantidades a comprar de cada producto", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, padx=50, pady=1)
    tk.Label(ventana, text="-Aceite para pestañas").grid(row=4, column=0, columnspan=1, padx=50, pady=1)
    caja1 = ttk.Entry(ventana, width=10)
    caja1.grid(row=5, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Labial mate").grid(row=6, column=0, columnspan=1, padx=50, pady=1)
    caja2 = ttk.Entry(ventana, width=10)
    caja2.grid(row=7, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Polvo traslucido").grid(row=8, column=0, columnspan=1, padx=50, pady=1)
    caja3 = ttk.Entry(ventana, width=10)
    caja3.grid(row=9, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Gloss").grid(row=10, column=0, columnspan=1, padx=50, pady=1)
    caja4 = ttk.Entry(ventana, width=10)
    caja4.grid(row=11, column=0, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Rizador de pestañas").grid(row=4, column=1, columnspan=3, padx=50, pady=1)
    caja5 = ttk.Entry(ventana, width=10)
    caja5.grid(row=5, column=1, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Delineado de ojos").grid(row=6, column=1, columnspan=3, padx=50, pady=1)
    caja6 = ttk.Entry(ventana, width=10)
    caja6.grid(row=7, column=1, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Labial").grid(row=8, column=1, columnspan=3, padx=50, pady=1)
    caja7 = ttk.Entry(ventana, width=10)
    caja7.grid(row=9, column=1, columnspan=1, padx=50, pady=1)
    tk.Label(ventana, text="-Polvo matificante").grid(row=10, column=1, columnspan=3, padx=50, pady=1)
    caja8 = ttk.Entry(ventana, width=10)
    caja8.grid(row=11, column=1, columnspan=1, padx=50, pady=1)
    def calcular():
        aceite = int(caja1.get())
        labialm = int(caja2.get())
        polvo = int(caja3.get())
        gloss = int(caja4.get())
        rizador = int(caja5.get())
        delineador = int(caja6.get())
        labial = int(caja7.get())
        polvom = int(caja8.get())
        aceitef = aceite * 60
        labialmf = labialm * 48
        polvof = polvo * 110
        glossf = gloss * 60 * 0.90
        rizadorf = rizador * 36
        delineadorf = delineador * 37
        labial1 = (labial // 2) + (labial % 2)
        labialf = labial1 * 49
        polvomf = polvom * 115
        final = aceitef + labialmf + polvof + glossf + rizadorf + delineadorf + labialf + polvomf
        global datos_cotizacion
        datos_cotizacion = {
            "Aceite": aceite,
            "Labial Mate": labialm,
            "Polvo Traslucido": polvo,
            "Gloss": gloss,
            "Rizador": rizador,
            "Delineador": delineador,
            "Labial 2x1": labial,
            "Polvo Matificante": polvom,
            "Total": final
        }
        if (aceite >= 0):
            if (labialm >= 0):
                if (polvo >= 0):
                    if (gloss >= 0):
                        if (rizador >= 0):
                            if (delineador >= 0):
                                if(labial >= 0):
                                    if (polvom >= 0):
                                        resultado_label.config(text=f"hola provedor el precio total a pagar de todo es ${final} pesos")
                                    else:
                                        resultado_label.config(text="Cantidades de polvo matificante invalidas")
                                else:
                                    resultado_label.config(text="Cantidades de labial invalidas")
                            else:
                                resultado_label.config(text="Cantidades de delineador invalidas")
                        else:
                            resultado_label.config(text="Cantidades de rizador de pestañas invalidas")
                    else:
                        resultado_label.config(text="Cantidades de gloss invalidas")
                else:
                    resultado_label.config(text="Cantidades de polvo traslucido invalidas")
            else:
                resultado_label.config(text="Cantidades de Labial mate invalidas")
        else:
            resultado_label.config(text="Cantidades de aceite para pestañas invalidas")
    ttk.Button(ventana, text="Ver precio total", command=calcular).grid(row=12, column=0, columnspan=2, padx=50, pady=1)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.grid(row=13, column=0, columnspan=2, padx=50, pady=1)

def mostrar_ventana6(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True, True, True, True, True, True, True, True])
    # Mostrar cotización calculada si existe
    if datos_cotizacion:
        texto = "Cotización actual:\n" + "\n".join(f"{k}: {v}" for k, v in datos_cotizacion.items())
    else:
        texto = "No hay cotización disponible."
    frame_izquierda = tk.Frame(ventana)
    frame_izquierda.grid(row=4, column=0, rowspan=20, sticky="nw")
 
    tk.Label(ventana, text=texto, font=("Arial", 12)).grid(row=4, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(frame_izquierda, text="Fresita makeup", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w")
    tk.Label(frame_izquierda, text="Codigo postal: 72100", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="w")
    tk.Label(frame_izquierda, text="Proveedor: Javier Garcia Perez", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="w")
    tk.Label(frame_izquierda, text="Distribuidora: Maquillate", font=("Arial", 12)).grid(row=3, column=0, pady=5, sticky="w")
    tk.Label(frame_izquierda, text="Entidad de emision: Puebla,Puebla", font=("Arial", 12)).grid(row=4, column=0, pady=5, sticky="w")
    tk.Label(frame_izquierda, text="Colonia de emision: Guadalupe Hidalgo", font=("Arial", 12)).grid(row=5, column=0, pady=5, sticky="w")
    tk.Label(ventana, text="_______________________").grid(row=5, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="firma encargado de recepcion").grid(row=6, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(frame_izquierda, text="_______________________").grid(row=6, column=0, pady=10, sticky="w")
    tk.Label(frame_izquierda, text="firma del provedor").grid(row=7, column=0, pady=10, sticky="w")




    





def mostrar_ventana7(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True, True, True, True, True, True, True, True ])

    global facturas

    tk.Label(ventana, text="Registro de Facturas", font=("Arial", 14)).grid(row=3, column=0, columnspan=3, pady=10)

    frame_lista = tk.Frame(ventana)
    frame_lista.grid(row=4, column=0, columnspan=3, sticky="w")

    # Mostrar facturas existentes (encabezados)
    for widget in frame_lista.winfo_children():
        widget.destroy()

    tk.Label(frame_lista, text="N°", width=5).grid(row=0, column=0)
    tk.Label(frame_lista, text="Fecha", width=15).grid(row=0, column=1)
    tk.Label(frame_lista, text="Monto", width=10).grid(row=0, column=2)

    for i, f in enumerate(facturas):
        tk.Label(frame_lista, text=f["numero"], width=5).grid(row=i+1, column=0)
        tk.Label(frame_lista, text=f["fecha"], width=15).grid(row=i+1, column=1)
        tk.Label(frame_lista, text=f"${f['monto']}", width=10).grid(row=i+1, column=2)

    # ================= AGREGAR FACTURA =================
    tk.Label(ventana, text="Agregar nueva factura", font=("Arial", 12)).grid(row=5, column=0, columnspan=3, pady=10)

    tk.Label(ventana, text="Fecha:").grid(row=6, column=0)
    entry_fecha = ttk.Entry(ventana)
    entry_fecha.grid(row=6, column=1)

    tk.Label(ventana, text="Monto:").grid(row=7, column=0)
    entry_monto = ttk.Entry(ventana)
    entry_monto.grid(row=7, column=1)

    def agregar_factura():
        fecha = entry_fecha.get().strip()
        monto_text = entry_monto.get().strip()
        if fecha == "" or monto_text == "":
            messagebox.showerror("Error", "Completa todos los campos")
            return
        try:
            monto_val = float(monto_text)
        except:
            messagebox.showerror("Error", "Monto inválido")
            return

        nuevo_num = facturas[-1]["numero"] + 1 if facturas else 1
        facturas.append({
            "numero": nuevo_num,
            "fecha": fecha,
            "monto": monto_val
        })
        mostrar_ventana7(ventana)

    ttk.Button(ventana, text="Agregar factura", command=agregar_factura).grid(row=8, column=0, columnspan=2, pady=10)

    
    tk.Label(ventana, text="Ingrese el numero de la factura que desea eliminar:").grid(row=9, column=0, pady=10)
    entry_eliminar = ttk.Entry(ventana)
    entry_eliminar.grid(row=9, column=1)

    def eliminar_factura():
        num_text = entry_eliminar.get().strip()
        try:
            num = int(num_text)
        except:
            messagebox.showerror("Error", "Número inválido")
            return

        for f in facturas:
            if f["numero"] == num:
                facturas.remove(f)
                messagebox.showinfo("Eliminado", f"Factura {num} eliminada")
                mostrar_ventana7(ventana)
                return
        messagebox.showerror("Error", "Factura no encontrada")

    ttk.Button(ventana, text="Eliminar", command=eliminar_factura).grid(row=10, column=0, columnspan=2, pady=10)

def mostrar_ventana8(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True]*8)

    # 🔧 CONFIG GRID (IMPORTANTE PARA QUE SE VEAN LOS BOTONES)
    ventana.grid_rowconfigure(3, weight=1)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    frame = tk.Frame(ventana, bg="black")
    frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="n")

    # 🔽 OBTENER DATOS
    try:
        doc_ref = db.collection("PERFIL").document("perfil")
        doc = doc_ref.get()

        if not doc.exists:
            messagebox.showerror("Error", "No existe el perfil")
            return

        data = doc.to_dict()

    except Exception as e:
        messagebox.showerror("Error", f"Error de conexión: {e}")
        return

    nombre = data.get("Nombre", "N/A")
    edad = data.get("Edad", "0")
    telefono = data.get("Telefono", "0")
    horario = data.get("Horario", "No definido")
    foto = data.get("Fotografia", "")

    # 🧾 LABELS
    estilo = {"bg": "black", "fg": "white", "font": ("Impact", 12)}

    tk.Label(frame, text="PERFIL", font=("Impact", 16),
             bg="black", fg="gold").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text=f"Nombre: {nombre}", **estilo).grid(row=1, column=0, columnspan=2)
    tk.Label(frame, text=f"Edad: {edad}", **estilo).grid(row=2, column=0, columnspan=2)
    tk.Label(frame, text=f"Teléfono: {telefono}", **estilo).grid(row=3, column=0, columnspan=2)
    tk.Label(frame, text=f"Horario: {horario}", **estilo).grid(row=4, column=0, columnspan=2)
    tk.Label(frame, text="Fotografia del entrenador:", **estilo).grid(row=5, column=0, columnspan=2)

    # 🖼️ IMAGEN
    label_img = tk.Label(frame, bg="black")
    label_img.grid(row=6, column=0, columnspan=2, pady=10)

    def cargar_imagen(ruta, label):
        if not ruta:
            label.config(text="Sin imagen", fg="gray")
            return

        if not os.path.exists(ruta):
            label.config(text="Ruta no encontrada", fg="red")
            return

        try:
            img = Image.open(ruta)
            img = img.resize((120, 120))
            img_tk = ImageTk.PhotoImage(img)

            label.config(image=img_tk, text="")
            label.image = img_tk
        except:
            label.config(text="Error al cargar imagen", fg="red")

    cargar_imagen(foto, label_img)

    # 🔐 CAMBIAR CONTRASEÑA
    def cambiar_contrasena():
        ventana_pass = tk.Toplevel(ventana)
        ventana_pass.title("Cambiar contraseña")
        ventana_pass.geometry("300x220")

        ventana_pass.transient(ventana)
        ventana_pass.grab_set()

        tk.Label(ventana_pass, text="Nueva contraseña").pack(pady=5)
        entry1 = tk.Entry(ventana_pass, show="*")
        entry1.pack(pady=5)

        tk.Label(ventana_pass, text="Confirmar contraseña").pack(pady=5)
        entry2 = tk.Entry(ventana_pass, show="*")
        entry2.pack(pady=5)

        def guardar():
            if entry1.get() == "" or entry2.get() == "":
                messagebox.showerror("Error", "Campos vacíos")
                return

            if entry1.get() != entry2.get():
                messagebox.showerror("Error", "No coinciden")
                return

            db.collection("CONTRASEÑA").document("contraseña").update({
                "contraseña": entry1.get()
            })

            messagebox.showinfo("Éxito", "Contraseña actualizada")
            ventana_pass.destroy()

        tk.Button(ventana_pass, text="Guardar", bg="green", fg="white",
                  command=guardar).pack(pady=15)

    # ✏️ MODIFICAR PERFIL
    def modificar_perfil():
        ventana_editar = tk.Toplevel(ventana)
        ventana_editar.title("Modificar perfil")
        ventana_editar.geometry("350x550")

        ventana_editar.transient(ventana)
        ventana_editar.grab_set()

        ruta_temp = [foto]

        campos = {
            "Nombre": nombre,
            "Edad": edad,
            "Teléfono": telefono,
            "Horario": horario
        }

        entries = {}

        for campo, valor in campos.items():
            tk.Label(ventana_editar, text=campo).pack()
            e = tk.Entry(ventana_editar)
            e.insert(0, valor)
            e.pack(pady=2)
            entries[campo] = e

        label_img_edit = tk.Label(ventana_editar)
        label_img_edit.pack(pady=10)
        cargar_imagen(ruta_temp[0], label_img_edit)

        def seleccionar_imagen():
            ruta = filedialog.askopenfilename(
                parent=ventana_editar,
                title="Seleccionar imagen",
                filetypes=[("Imágenes", "*.jpg *.png *.jpeg *.webp")]
            )

            if ruta:
                ruta_temp[0] = ruta
                cargar_imagen(ruta, label_img_edit)

            ventana_editar.lift()
            ventana_editar.focus_force()

        tk.Button(ventana_editar, text="Cambiar imagen",
                  command=seleccionar_imagen).pack(pady=5)

        def guardar():
            try:
                nuevos = {
                    "Nombre": entries["Nombre"].get(),
                    "Edad": int(entries["Edad"].get()),
                    "Telefono": int(entries["Teléfono"].get()),
                    "Horario": entries["Horario"].get(),
                    "Fotografia": ruta_temp[0]
                }

                db.collection("PERFIL").document("perfil").update(nuevos)

                messagebox.showinfo("Éxito", "Perfil actualizado")
                ventana_editar.destroy()
                mostrar_ventana8(ventana)

            except:
                messagebox.showerror("Error", "Datos inválidos")

        tk.Button(ventana_editar, text="Guardar cambios",
                  bg="green", fg="white",
                  command=guardar).pack(pady=15)

    # 🔘 BOTONES
    tk.Button(frame, text="Cambiar contraseña",
              font=("Impact", 12),
              bg="yellow",
              command=cambiar_contrasena).grid(row=7, column=0, padx=5, pady=20)

    tk.Button(frame, text="Modificar perfil",
              font=("Impact", 12),
              bg="red", fg="white",
              command=modificar_perfil).grid(row=7, column=1, padx=5, pady=20)

if __name__ == "__main__":
    mostrar_ventana1()