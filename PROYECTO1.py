import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import ttk
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
    b3 = ttk.Button(frame_botones, text="Pedidos y Mensaje", style="BotonNegro.TButton", command=lambda: mostrar_ventana3(ventana))
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

    tk.Label(ventana, text="Inicio", font=("Arial", 12)).grid(row=4, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Visión: Ser tu distribuidora de maquillajes número uno", font=("Arial", 12)).grid(row=5, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Misión: Darte el mejor precio, calidad y hacerte feliz", font=("Arial", 12)).grid(row=6, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Ubicación: CBTIs 260, Puebla de Zaragoza, México", font=("Arial", 12)).grid(row=7, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Logros de la empresa:").grid(row=8, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Vender mas de 10,000 pesos en menos de 6 meses").grid(row=9, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Ser de los mejores repartidores de maquillaje").grid(row=10, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Ofrecer una gran calidad precio en productos segun los clientes").grid(row=11, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="-Lograr una excelente cantidad de clientes frecuentes").grid(row=12, column=0, columnspan=3, padx=50, pady=10)
def mostrar_ventana3(ventana):
    limpiar_ventana(ventana)
    crear_marco_superior(ventana)
    crear_imagenes_inferiores(ventana)
    crear_botones(ventana, [True, True, True, True, True, True, True, True])

    tk.Label(ventana, text="Contacto", font=("Arial", 12)).grid(row=3, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text="Ingresa tu mensaje:", font=("Arial", 12)).grid(row=4, column=0, columnspan=1, padx=50, pady=10)
    caja = ttk.Entry(ventana, width=50)
    caja.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
    ttk.Button(ventana, text="Mandar", command=lambda: print("Mensaje:", caja.get())).grid(row=6, column=0, columnspan=1, pady=10)
    tk.Label(ventana, text="Pedidos:", font=("Arial", 12)).grid(row=3, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="-Aceite para pestañas 5 piezas", font=("Arial", 12)).grid(row=4, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="-Labial 10 piezas", font=("Arial", 12)).grid(row=5, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="-Polvo matificante 5 piezas", font=("Arial", 12)).grid(row=6, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="-Gloss 10 piezas", font=("Arial", 12)).grid(row=7, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="-Labial mate 10 piezas", font=("Arial", 12)).grid(row=8, column=1, columnspan=2, padx=50, pady=10)
    tk.Label(ventana, text="-Lista de contactos:", font=("Arial", 12)).grid(row=9, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text=">Empleados recepcion: 2213892909").grid(row=10, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text=">Jefe de empresa: 8790764567").grid(row=11, column=0, columnspan=1, padx=50, pady=10)
    tk.Label(ventana, text=">Encargado de recepcion: 0989201898").grid(row=12, column=0, columnspan=1, padx=50, pady=10)


    

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
    crear_botones(ventana, [True, True, True, True, True, True, True, True])

    global CONTRASENA

    tk.Label(ventana, text="Perfil del Proveedor", font=("Arial", 12)).grid(row=3, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Nombre: Javier").grid(row=4, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Apellido paterno: Garcia").grid(row=5, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Apellido materno: Perez").grid(row=6, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Distribuidora: Maquilladist").grid(row=7, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Numero de telefono: 2213753278").grid(row=8, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Correo electronico: garciaperezjavier.cb260@gmail.com").grid(row=9, column=0, columnspan=3, padx=50, pady=10)
    tk.Label(ventana, text="Fecha en la que se unio: 01/09/2025").grid(row=10, column=0, columnspan=3, padx=50, pady=10)

    tk.Label(ventana, text="Cambiar contraseña").grid(row=11, column=0, columnspan=2, pady=10)

    tk.Label(ventana, text="Nueva contraseña:").grid(row=12, column=0, pady=10)


    nueva_pass = ttk.Entry(ventana, width=20)
    nueva_pass.grid(row=12, column=1, pady=10)

    
    def guardar_contraseña():
        nueva = nueva_pass.get().strip()

        if nueva == "":
            messagebox.showerror("Error", "La contraseña no puede estar vacía")
            return   

    
        CONTRASENA.set(nueva)

        messagebox.showinfo("Éxito", "Contraseña guardada correctamente")

    ttk.Button(ventana, text="Guardar", command=guardar_contraseña).grid(row=13, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    mostrar_ventana1()