import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# --- LÓGICA DE PERSISTENCIA (ARCHIVOS) ---
FILE_RUTAS = "rutas.json"
FILE_REGISTROS = "registros.json"

def cargar_datos():
    """Carga los datos desde los archivos JSON al iniciar."""
    global lista_rutas, lista_registros
    
    # Cargar Rutas
    if os.path.exists(FILE_RUTAS):
        with open(FILE_RUTAS, "r", encoding="utf-8") as f:
            lista_rutas = json.load(f)
    else:
        # Datos iniciales si el archivo no existe
        lista_rutas = [
            {"nombre": "U-102 (R20)", "info": "R-20: Centro - Ojocaliente | 06:00 - 21:30"},
            {"nombre": "U-045 (R40)", "info": "R-40: Terminal Sur - UAA | 06:15 - 22:00"}
        ]

    # Cargar Registros
    if os.path.exists(FILE_REGISTROS):
        with open(FILE_REGISTROS, "r", encoding="utf-8") as f:
            # Convertimos de nuevo a tuplas para que el Treeview no tenga problemas
            data = json.load(f)
            lista_registros = [tuple(x) for x in data]
    else:
        lista_registros = []

def guardar_datos():
    """Guarda las listas actuales en los archivos JSON."""
    with open(FILE_RUTAS, "w", encoding="utf-8") as f:
        json.dump(lista_rutas, f, indent=4, ensure_ascii=False)
    
    with open(FILE_REGISTROS, "w", encoding="utf-8") as f:
        json.dump(lista_registros, f, indent=4, ensure_ascii=False)

# Inicializamos la carga de datos antes de crear la GUI
cargar_datos()

# --- VISTAS Y FUNCIONES LÓGICAS ---
def limpiar_contenido():
    for widget in contenido.winfo_children():
        widget.destroy()

def mostrar_registro():
    limpiar_contenido()
    
    titulo_seccion = tk.Label(contenido, text="Registro de Movilidad", bg=color_content, fg=color_header, font=("Segoe UI", 16, "bold"))
    titulo_seccion.grid(row=0, column=0, columnspan=2, pady=(20, 20), padx=30, sticky="w")

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

        nuevo_registro = (nombre, apellido, rol.capitalize(), matricula, unidad)
        lista_registros.append(nuevo_registro)
        
        # GUARDAR CAMBIOS EN ARCHIVO
        guardar_datos()
        
        tabla.insert("", tk.END, values=nuevo_registro)
        
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_matricula.delete(0, tk.END)
        combo_unidades.set("")
        rol_var.set("usuario")
        toggle_matricula()

    # Formulario (Grid)
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

    btn_guardar = tk.Button(contenido, text="Confirmar Registro", bg="#41C9E2", fg="white", font=("Segoe UI", 11, "bold"), width=20, command=guardar_registro)
    btn_guardar.grid(row=6, column=0, columnspan=2, pady=20, padx=30, sticky="w")

    # Tabla
    columnas = ("nombre", "apellido", "rol", "matricula", "unidad")
    tabla = ttk.Treeview(contenido, columns=columnas, show="headings", height=8)
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
        tabla.column(col, width=100)
    tabla.grid(row=7, column=0, columnspan=2, padx=30, pady=10, sticky="nsew")

    for reg in lista_registros:
        tabla.insert("", tk.END, values=reg)

def mostrar_terminal():
    limpiar_contenido()
    tk.Label(contenido, text="Terminal de Rutas Activas", bg=color_content, fg="#124076", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(20, 10), padx=30)
    
    cols = ("UNIDAD", "INFORMACIÓN COMPLETA DE LA RUTA")
    tabla_term = ttk.Treeview(contenido, columns=cols, show="headings", height=15)
    tabla_term.heading(cols[0], text=cols[0])
    tabla_term.heading(cols[1], text=cols[1])
    
    for r in lista_rutas:
        tabla_term.insert("", tk.END, values=(r["nombre"], r["info"]))
    tabla_term.pack(padx=30, pady=10, fill="both", expand=True)

def mostrar_asignar():
    limpiar_contenido()
    tk.Label(contenido, text="Agregar Nueva Unidad", bg=color_content, fg="#124076", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(20, 20), padx=30, sticky="w")
    
    tk.Label(contenido, text="ID Unidad:", bg=color_content).grid(row=1, column=0, sticky="w", padx=30)
    ent_id = tk.Entry(contenido, width=40)
    ent_id.grid(row=1, column=1, pady=5)

    tk.Label(contenido, text="Info Completa:", bg=color_content).grid(row=2, column=0, sticky="w", padx=30)
    ent_full = tk.Entry(contenido, width=40)
    ent_full.grid(row=2, column=1, pady=5)

    def agregar_nueva_ruta():
        nombre = ent_id.get()
        info = ent_full.get()
        if nombre and info:
            lista_rutas.append({"nombre": nombre, "info": info})
            # GUARDAR CAMBIOS EN ARCHIVO
            guardar_datos()
            messagebox.showinfo("Éxito", f"Unidad {nombre} guardada.")
            ent_id.delete(0, tk.END)
            ent_full.delete(0, tk.END)

    tk.Button(contenido, text="Guardar Unidad", bg="#41C9E2", fg="white", command=agregar_nueva_ruta).grid(row=3, column=0, columnspan=2, pady=20)

# --- CONFIGURACIÓN VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Sistema R-UTA-S (Persistente)")
ventana.geometry("1000x650")

color_header = "#124076"
color_menu = "#1F3C88"
color_button = "#41C9E2"
color_exit = "#2C3E50"
color_content = "#FFFFFF"

# Estructura de la GUI (Encabezado, Menú, Contenido)
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")
tk.Label(encabezado, text="Gestión de Transporte Público R-UTA-S", bg=color_header, fg="white", font=("Segoe UI", 20, "bold")).place(x=20, y=15)

menu = tk.Frame(ventana, bg=color_menu, width=220)
menu.pack(side="left", fill="y")

tk.Button(menu, text="Registro Perfil", bg=color_menu, fg="white", command=mostrar_registro, relief="flat").pack(fill="x", pady=15)
tk.Button(menu, text="Terminal de Rutas", bg=color_menu, fg="white", command=mostrar_terminal, relief="flat").pack(fill="x", pady=15)
tk.Button(menu, text="Asignar Unidad", bg=color_menu, fg="white", command=mostrar_asignar, relief="flat").pack(fill="x", pady=15)

tk.Button(menu, text="Salir", bg=color_exit, fg="white", command=ventana.destroy).pack(side="bottom", fill="x", pady=20)

contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True, padx=20, pady=20)

style = ttk.Style()
style.theme_use("clam")

mostrar_registro()
ventana.mainloop()
