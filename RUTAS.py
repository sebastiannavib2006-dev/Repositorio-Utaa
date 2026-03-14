# PROYECTO DE PROGRAMACIÓN: SISTEMA DE MOVILIDAD
#RUTAS
# Estilo: Programación Estructurada (Funciones y Diccionarios)

def obtener_tipo_usuario():#def para obtener el tipo de usuario (conductor o usuario) y validar la entrada
    #Pregunta el rol del usuario y valida la entrada
    while True:#while para asegurar que el usuario ingrese una opción válida
        print("\n========================================")
        print("---- BIENVENIDO AL ÁREA DE MOVILIDAD ---")
        print("========================================")  
        print("---------1. Conductor-------------------")
        print("---------2. Usuario---------------------")
        opcion = input("----------Selecciona una opción (1 o 2): ")
        print("========================================\n")
        
        match opcion:
            case "1":
                return "Conductor"
            case "2":
                return "Usuario"
            case _:
                print("Opción no válida. Por favor, escribe 1 o 2.")

#Función para registrar al conductor, solicitando su información y guardándola.
#De aqui 
def registrar_conductor():
    #Solicita datos al conductor y los guarda en un diccionario.
    print("\n--- REGISTRO DE CONDUCTOR ---")
    datos = {
        "nombre": input("Ingresa tu nombre: "),
        "apellido": input("Ingresa tu apellido: "),
        "edad": input("Ingresa tu edad: "),
        "licencia": input("Ingresa tu número de licencia: ")
    }
    return datos #Datos guardados en 'datos' y retornados para su uso posterior.

def mostrar_perfil_conductor(conductor):
    #Muestra de forma limpia la información guardada.
    print("\n===============================")
    print("      PERFIL DEL CONDUCTOR     ")
    print("===============================")
    print(f"Nombre Completo: {conductor['nombre']} {conductor['apellido']}")
    print(f"Edad:            {conductor['edad']} años")
    print(f"No. Licencia:    {conductor['licencia']}")
    print("===============================\n") #Hasta aqui lo del conductor

#Funion para registrar al usuario de transporte público, solicitando su información y guardándola
def registrar_usuario():
    #Solicita datos al usuario y los guarda en un diccionario.
    print("\n--- REGISTRO DE USUARIO ---")
    datos = {
        "nombre": input("Ingresa tu nombre: "),
        "apellido": input("Ingresa tu apellido: "),
        "edad": input("Ingresa tu edad: ")
    }
    return datos
def mostrar_perfil_usuario(usuario):
    #Muestra de forma limpia la información guardada.
    print("\n===============================")
    print("      PERFIL DEL USUARIO     ")
    print("===============================")
    print(f"Nombre Completo: {usuario['nombre']} {usuario['apellido']}")
    print(f"Edad:            {usuario['edad']} años")
    print("===============================\n") #Hasta aqui lo del conductor

#Lista de datos para camiones y rutas (simulada con diccionarios)
camiones = {
    # Lista de camiones disponibles con su unidad y ruta asignada
    "Camión 1": {"unidad": "U-102", "ruta": "Ruta 20"},
    "Camión 2": {"unidad": "U-045", "ruta": "Ruta 40"},
    "Camión 3": {"unidad": "U-088", "ruta": "Ruta 50"},
    "Camión 4": {"unidad": "U-156", "ruta": "Ruta 60"},
    "Camión 5": {"unidad": "U-200", "ruta": "Ruta 70"}
}
#Aqui vamos a poner las rutas disponibles para los conductores
def asignar_unidad():
    print("\n--- ASIGNACIÓN DE UNIDAD ---")
    print("Unidades disponibles hoy:")
    print("1. Unidad U-102 (Ruta 20)")
    print("2. Unidad U-045 (Ruta 40)")
    print("3. Unidad U-088 (Ruta 50)")
    print("4. Unidad U-156 (Ruta 60)")
    print("5. Unidad U-200 (Ruta 70)")
    
    seleccion = input("Selecciona el número de unidad que tomarás: ")
    
    match seleccion:
        case "1":
            return "U-102 de la Ruta 20"
        case "2":
            return "U-045 de la Ruta 40"
        case "3":
            return "U-088 de la Ruta 50"
        case "4":
            return "U-156 de la Ruta 60"
        case "5":
            return "U-200 de la Ruta 70"
        case _:
            print("Selección inválida, no se asignará unidad.")

#En este bloque vamos a poner datos para el usuario, como horarios y paradas de las rutas disponibles
def seleccionar_ruta():
    print("\n--- RUTAS DISPONIBLES ---")
    print("1. R-20: Centro - Ojocaliente, Paradas: Madero, 2do Anillo, Horario: 06:00 - 21:30")
    print("2. R-40: Terminal Sur - Universidad, Paradas: Av. Universidad, 1er Anillo, Horario: 06:15 - 22:00")
    print("3. R-50: Lomas de Ajedrez - Hospital, Paradas: Tercer Anillo, Clínica 2, Horario: 05:45 - 21:00")
    print("4. R-60: Plaza de Armas - Fraccionamiento, Paradas: Av. Siglo XXI, 4to Anillo, Horario: 06:30 - 22:30")
    print("5. R-70: Parque Industrial - Zona Centro, Paradas: Av. Aguascalientes, 3er Anillo, Horario: 05:30 - 21:45")
    
    elegir_ruta = input("\nSelecciona una ruta para ver detalles (1-5): ")

    match elegir_ruta:
        case "1":
            return "R-20: Centro - Ojocaliente, Paradas: Madero, 2do Anillo, Horario: 06:00 - 21:30"
        case "2":
            return "R-40: Terminal Sur - Universidad, Paradas: Av. Universidad, 1er Anillo, Horario: 06:15 - 22:00"
        case "3":
            return "R-50: Lomas de Ajedrez - Hospital, Paradas: Tercer Anillo, Clínica 2, Horario: 05:45 - 21:00"
        case "4":
            return "R-60: Plaza de Armas - Fraccionamiento, Paradas: Av. Siglo XXI, 4to Anillo, Horario: 06:30 - 22:30"
        case "5":
            return "R-70: Parque Industrial - Zona Centro, Paradas: Av. Aguascalientes, 3er Anillo, Horario: 05:30 - 21:45"
        case _:
            print("Selección inválida.")
            return None

def inicio(): # Función principal que inicia el programa y gestiona el flujo
    while True:
        usu = obtener_tipo_usuario()
        
        match usu:
            case "Conductor":
                # 1. Registramos y mostramos perfil
                datos_c = registrar_conductor()
                mostrar_perfil_conductor(datos_c)
                
                # 2. Asignamos la unidad
                unidad_asignada = asignar_unidad()
                print(f"\nCONFIRMADO: El chofer {datos_c['nombre']} operará la unidad {unidad_asignada}.")
                break # Salimos del programa después de asignar la unidad al conductor
                
            case "Usuario":
                # 1. Registro del usuario
                datos_u = registrar_usuario()
                mostrar_perfil_usuario(datos_u)
                
                # 2. Mostrar información de transporte
                print("\nAcceso concedido.")
                print("Las rutas, horarios y paradas serian las siguientes...")
                ruta_seleccionada = seleccionar_ruta()
                if ruta_seleccionada:
                    print(f"\nDetalles: {ruta_seleccionada}")
                print(f"Bienvenido {datos_u['nombre']}, ¡buen viaje!")
                break
            case "Salir":
                print("Saliendo del programa... ¡Buen viaje!")
                break
            case _:
                print("Opción no reconocida.")
if __name__ == "__main__":    inicio()