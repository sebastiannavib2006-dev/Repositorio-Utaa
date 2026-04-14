import tkinter as tk
from tkinter import ttk, messagebox

# Datos Globales (Simulación de Base de Datos)
lista_rutas = [
    {"nombre": "U-102 (R20)", "info": "R-20: Centro - Ojocaliente | 06:00 - 21:30"},
    {"nombre": "U-045 (R40)", "info": "R-40: Terminal Sur - UAA | 06:15 - 22:00"}
]

# Lista para guardar a las personas registradas y no perderlas al cambiar de pestaña
lista_registros = []

# Funciones Lógicas y Vistas
def limpiar_contenido():
    """Limpia el área derecha para cargar una nueva sección."""
    for widget in contenido.winfo_children():
        widget.destroy()

# --- SECCIÓN 1: REGISTRO PERFIL ---
def mostrar_registro():
    limpiar_contenido()
    
    titulo_seccion = tk.Label(contenido, text="Registro de Movilidad", bg=color_content, fg=color_header, font=("Segoe UI", 16, "bold"))
    titulo_seccion.grid(row=0, column=0, columnspan=2, pady=(20, 20), padx=30, sticky="w")

    # Variables de control
    rol_var = tk.StringVar(value="usuario")

    def toggle_matricula():
        if rol_var.get() == "conductor":
            entrada_matricula.config(state="normal")
        else:
            entrada_matricula.delete(0, tk.END)
            entrada_matricula.config(state="disabled")

    def guardar_registro():
        nombre = entrada_nombre.get()
        apellido = entrada_apellido.get()
        rol = rol_var.get()
        unidad = combo_unidades.get()
        matricula = entrada_matricula.get() if rol == "conductor" else "N/A"

        if not nombre or not apellido or not unidad:
            messagebox.showwarning("Atención", "Por favor completa Nombre, Apellido y selecciona una Unidad.")
            return

        # Guardar en memoria y en la tabla
        nuevo_registro = (nombre, apellido, rol.capitalize(), matricula, unidad)
        lista_registros.append(nuevo_registro)
        tabla.insert("", tk.END, values=nuevo_registro)
        
        # Limpiar
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_matricula.delete(0, tk.END)
        combo_unidades.set("")
        rol_var.set("usuario")
        toggle_matricula()

    # Formulario alineado a la izquierda (Grid)
    tk.Label(contenido, text="Nombre:", bg=color_content, font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w", padx=30, pady=5)
    entrada_nombre = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
    entrada_nombre.grid(row=1, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Apellido:", bg=color_content, font=("Segoe UI", 11)).grid(row=2, column=0, sticky="w", padx=30, pady=5)
    entrada_apellido = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
    entrada_apellido.grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Rol:", bg=color_content, font=("Segoe UI", 11)).grid(row=3, column=0, sticky="w", padx=30, pady=5)
    frame_radio = tk.Frame(contenido, bg=color_content)
    frame_radio.grid(row=3, column=1, sticky="w", pady=5)
    tk.Radiobutton(frame_radio, text="Usuario", variable=rol_var, value="usuario", bg=color_content, font=("Segoe UI", 10), command=toggle_matricula).pack(side="left")
    tk.Radiobutton(frame_radio, text="Conductor", variable=rol_var, value="conductor", bg=color_content, font=("Segoe UI", 10), command=toggle_matricula).pack(side="left", padx=10)

    tk.Label(contenido, text="Matrícula:", bg=color_content, font=("Segoe UI", 11)).grid(row=4, column=0, sticky="w", padx=30, pady=5)
    entrada_matricula = tk.Entry(contenido, width=30, font=("Segoe UI", 11), state="disabled")
    entrada_matricula.grid(row=4, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Unidad/Ruta:", bg=color_content, font=("Segoe UI", 11)).grid(row=5, column=0, sticky="w", padx=30, pady=5)
    combo_unidades = ttk.Combobox(contenido, width=28, font=("Segoe UI", 11), values=[r["nombre"] for r in lista_rutas], state="readonly")
    combo_unidades.grid(row=5, column=1, sticky="w", pady=5)

    btn_guardar = tk.Button(contenido, text="Confirmar Registro", bg=color_button, fg="white", font=("Segoe UI", 11, "bold"), width=20, command=guardar_registro)
    btn_guardar.grid(row=6, column=0, columnspan=2, pady=20, padx=30, sticky="w")

    # Tabla de Datos
    columnas = ("nombre", "apellido", "rol", "matricula", "unidad")
    tabla = ttk.Treeview(contenido, columns=columnas, show="headings", height=8)
    
    tabla.heading("nombre", text="Nombre")
    tabla.heading("apellido", text="Apellido")
    tabla.heading("rol", text="Rol")
    tabla.heading("matricula", text="Matrícula")
    tabla.heading("unidad", text="Unidad")
    
    tabla.column("nombre", width=120)
    tabla.column("apellido", width=120)
    tabla.column("rol", width=100)
    tabla.column("matricula", width=100)
    tabla.column("unidad", width=150)

    tabla.grid(row=7, column=0, columnspan=2, padx=30, pady=10, sticky="nsew")

    # Cargar datos previos si se cambió de pestaña
    for reg in lista_registros:
        tabla.insert("", tk.END, values=reg)

#SECCIÓN 2: TERMINAL DE RUTAS
def mostrar_terminal():
    limpiar_contenido()
    
    titulo_seccion = tk.Label(contenido, text="Terminal de Rutas Activas", bg=color_content, fg=color_header, font=("Segoe UI", 16, "bold"))
    titulo_seccion.pack(anchor="w", pady=(20, 10), padx=30)
    
    info_label = tk.Label(contenido, text="Consulta de itinerarios y unidades disponibles en la red.", bg=color_content, font=("Segoe UI", 11), fg="#555555")
    info_label.pack(anchor="w", padx=30, pady=(0, 10))

    cols = ("UNIDAD", "INFORMACIÓN COMPLETA DE LA RUTA")
    tabla_term = ttk.Treeview(contenido, columns=cols, show="headings", height=15)
    
    tabla_term.heading(cols[0], text=cols[0])
    tabla_term.heading(cols[1], text=cols[1])
    tabla_term.column(cols[0], width=150)
    tabla_term.column(cols[1], width=500)
    
    for r in lista_rutas:
        tabla_term.insert("", tk.END, values=(r["nombre"], r["info"]))
    
    tabla_term.pack(padx=30, pady=10, fill="both", expand=True)

#SECCIÓN 3: ASIGNAR UNIDAD
def mostrar_asignar():
    limpiar_contenido()
    
    titulo_seccion = tk.Label(contenido, text="Agregar Nueva Unidad a la Red", bg=color_content, fg=color_header, font=("Segoe UI", 16, "bold"))
    titulo_seccion.grid(row=0, column=0, columnspan=2, pady=(20, 20), padx=30, sticky="w")
    
    tk.Label(contenido, text="Identificador de Unidad:", bg=color_content, font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w", padx=30, pady=5)
    ent_id = tk.Entry(contenido, width=40, font=("Segoe UI", 11))
    ent_id.grid(row=1, column=1, sticky="w", pady=5)
    tk.Label(contenido, text="(Ej. U-200 (R70))", bg=color_content, font=("Segoe UI", 9), fg="gray").grid(row=2, column=1, sticky="w", padx=0)

    tk.Label(contenido, text="Información Completa:", bg=color_content, font=("Segoe UI", 11)).grid(row=3, column=0, sticky="w", padx=30, pady=15)
    ent_full = tk.Entry(contenido, width=50, font=("Segoe UI", 11))
    ent_full.grid(row=3, column=1, sticky="w", pady=15)
    tk.Label(contenido, text="(Ej. R-70: Norte - Sur | Horario: 05:30 - 23:00)", bg=color_content, font=("Segoe UI", 9), fg="gray").grid(row=4, column=1, sticky="w", padx=0)

    def agregar_nueva_ruta():
        nombre = ent_id.get()
        info = ent_full.get()
        if nombre and info:
            lista_rutas.append({"nombre": nombre, "info": info})
            messagebox.showinfo("Éxito", f"La unidad {nombre} ha sido agregada exitosamente.")
            ent_id.delete(0, tk.END)
            ent_full.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Ambos campos son obligatorios para registrar la unidad.")

    btn_agregar = tk.Button(contenido, text="Guardar Unidad", bg=color_button, fg="white", font=("Segoe UI", 11, "bold"), width=20, command=agregar_nueva_ruta)
    btn_agregar.grid(row=5, column=0, columnspan=2, pady=30, padx=30, sticky="w")

# Configuración Visual Principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Movilidad - R-UTA-S")
ventana.geometry("1000x650")

# Paleta de colores ajustada a Azules y Blancos
color_header = "#124076"  # Azul profundo
color_menu = "#1F3C88"    # Azul medio
color_button = "#41C9E2"  # Azul claro vibrante
color_exit = "#2C3E50"    # Azul acero oscuro (para botón salir)
color_content = "#FFFFFF" # Blanco puro
color_bg_app = "#F0F4F8"  # Blanco/Grisáceo muy tenue para el fondo base

ventana.configure(bg=color_bg_app)

# Encabezado
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")
tk.Label(encabezado, text="Gestión de Transporte Público R-UTA-S", bg=color_header, fg="white", font=("Segoe UI", 20, "bold")).place(x=20, y=15)

# Menú Lateral
menu = tk.Frame(ventana, bg=color_menu, width=220)
menu.pack(side="left", fill="y")

# Botones del menú
tk.Button(menu, text="Registro Perfil", bg=color_menu, fg="white", activebackground=color_header, activeforeground="white", relief="flat", font=("Segoe UI", 12), command=mostrar_registro).pack(fill="x", pady=15, padx=10)
tk.Button(menu, text="Terminal de Rutas", bg=color_menu, fg="white", activebackground=color_header, activeforeground="white", relief="flat", font=("Segoe UI", 12), command=mostrar_terminal).pack(fill="x", pady=15, padx=10)
tk.Button(menu, text="Asignar Unidad", bg=color_menu, fg="white", activebackground=color_header, activeforeground="white", relief="flat", font=("Segoe UI", 12), command=mostrar_asignar).pack(fill="x", pady=15, padx=10)

# Espacio flexible para empujar el botón salir al fondo
spacer = tk.Label(menu, bg=color_menu)
spacer.pack(fill="both", expand=True)

# Botón Salir
tk.Button(menu, text="Salir del Sistema", bg=color_exit, fg="white", activebackground="#1A252F", activeforeground="white", relief="flat", font=("Segoe UI", 12, "bold"), command=ventana.quit).pack(fill="x", pady=20, padx=10)

# Área de Contenido
contenido = tk.Frame(ventana, bg=color_content, relief="flat")
contenido.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# Inicializar estilos de Treeview para que coincida con el diseño blanco/azul
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background=color_menu, foreground="white")
style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="white", fieldbackground="white")
style.map("Treeview", background=[("selected", color_button)])

# Cargar la primera vista por defecto
mostrar_registro()
ventana.mainloop()
