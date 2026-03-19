import tkinter as tk
from tkinter import ttk

# ==========================================
# Ventana principal - Proyecto R-UTA-S
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Movilidad - R-UTA-S")
ventana.geometry("900x550")
ventana.configure(bg="#F2F2F2")

# Colores principales (Mantenidos del código base)
color_header = "#1F3C88"
color_menu = "#162447"
color_button = "#1F78D1"
color_content = "#FFFFFF"

# ==========================================
# Encabezado
# ==========================================
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")

# Título adaptado a tu proyecto
titulo = tk.Label(encabezado, text="Gestión de Transporte Público R-UTA-S", bg=color_header, fg="white", font=("Segoe UI", 20, "bold"))
titulo.place(x=20, y=15)

# ==========================================
# Menú lateral
# ==========================================
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

# Botones del menú adaptados a tus funciones
btn_registro = tk.Button(menu, text="Registro Perfil", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_registro.pack(fill="x", pady=8)

btn_rutas = tk.Button(menu, text="Terminal de Rutas", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_rutas.pack(fill="x", pady=8)

btn_unidades = tk.Button(menu, text="Asignar Unidad", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_unidades.pack(fill="x", pady=8)

# ==========================================
# Área de contenido
# ==========================================
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True)

titulo_seccion = tk.Label(contenido, text="Registro de Movilidad", bg=color_content, fg="#333333", font=("Segoe UI", 16, "bold"))
titulo_seccion.place(x=30, y=20)

# ==========================================
# Widgets del formulario (Adaptados a tu código)
# ==========================================

# Etiqueta + Entry Nombre (registrar_conductor / registrar_usuario)
lbl_nombre = tk.Label(contenido, text="Nombre:", bg=color_content, font=("Segoe UI", 12))
lbl_nombre.place(x=30, y=80)

entrada_nombre = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_nombre.place(x=120, y=80)

# Etiqueta + Entry Apellido
lbl_apellido = tk.Label(contenido, text="Apellido:", bg=color_content, font=("Segoe UI", 12))
lbl_apellido.place(x=30, y=120)

entrada_apellido = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_apellido.place(x=120, y=120)

# RadioButtons para elegir el Rol (obtener_tipo_usuario)
lbl_rol = tk.Label(contenido, text="Rol:", bg=color_content, font=("Segoe UI", 12))
lbl_rol.place(x=30, y=170)

rol_seleccionado = tk.StringVar()
rb_conductor = tk.Radiobutton(contenido, text="Conductor", variable=rol_seleccionado, value="conductor", bg=color_content, font=("Segoe UI", 11))
rb_conductor.place(x=120, y=170)

rb_usuario = tk.Radiobutton(contenido, text="Usuario", variable=rol_seleccionado, value="usuario", bg=color_content, font=("Segoe UI", 11))
rb_usuario.place(x=230, y=170)

# Combobox para Unidades (asignar_unidad)
lbl_unidad = tk.Label(contenido, text="Unidad:", bg=color_content, font=("Segoe UI", 12))
lbl_unidad.place(x=30, y=210)

combo_unidades = ttk.Combobox(contenido, width=27, font=("Segoe UI", 11), values=["U-102 (R20)", "U-045 (R40)", "U-088 (R50)", "U-156 (R60)", "U-200 (R70)"])
combo_unidades.place(x=120, y=210)

# CheckButtons para Turnos (Extra para diseño profesional)
lbl_turnos = tk.Label(contenido, text="Turnos:", bg=color_content, font=("Segoe UI", 12))
lbl_turnos.place(x=30, y=250)

chk1 = tk.Checkbutton(contenido, text="Matutino", bg=color_content, font=("Segoe UI", 11))
chk1.place(x=120, y=250)

chk2 = tk.Checkbutton(contenido, text="Vespertino", bg=color_content, font=("Segoe UI", 11))
chk2.place(x=220, y=250)

# Caja de información de Rutas (seleccionar_ruta)
lbl_rutas_info = tk.Label(contenido, text="Información de la Ruta Seleccionada:", bg=color_content, font=("Segoe UI", 12))
lbl_rutas_info.place(x=30, y=300)

caja_rutas = tk.Text(contenido, width=65, height=5, font=("Segoe UI", 10), bd=1, relief="solid")
caja_rutas.place(x=30, y=330)
# Texto de ejemplo basado en tu código
caja_rutas.insert("1.0", "R-20: Centro - Ojocaliente | Horario: 06:00 - 21:30\nR-40: Terminal Sur - Universidad | Horario: 06:15 - 22:00")

# Botón principal adaptado
btn_guardar = tk.Button(contenido, text="Confirmar Registro", bg=color_button, fg="white", font=("Segoe UI", 12, "bold"), width=20)
btn_guardar.place(x=300, y=450)

ventana.mainloop()