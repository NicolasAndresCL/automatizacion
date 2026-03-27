# ejercicio funcion
contador = 0

def aumentar():
    global contador
    contador = contador + 1
    print(contador)

aumentar()
aumentar()
aumentar()          


def saludar():
    print("Hola, ¿cómo estás?")

saludar()

def mensaje():
    print("Hola Mundo")

mensaje()


def saludar():
    """
    Esta función devuelve el mensaje 'HOLA MUNDO 2'
    """
    return "HOLA MUNDO 2"

resultado = saludar()
print(resultado)



saludar = lambda: "HOLA MUNDO 2"

print(saludar())


def sumar_dos_numeros(num1, num2):
    """
    Recibe dos números como parámetros y retorna su suma.
    """
    resultado = num1 + num2
    return resultado


print(sumar_dos_numeros(5, 7)) 


# Sin input, añado un apellido2, por que tengo dos apellidos

def bienvenida(nombre, apellido, apellido2):
    return f"Bienvenido {nombre} {apellido} {apellido2}"

print(bienvenida("Nicolás", "Cano", "Leal"))

# Con input

def bienvenida(nombre, apellido, apellido2):
    return f"Bienvenido {nombre} {apellido} {apellido2}"

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
apellido2 = input("Ingresa tu segundo apellido: ")

print(bienvenida(nombre, apellido, apellido2))

# Opción ribusta, con validación de datos y manejo de espacios

def bienvenida(nombre, apellido, apellido2=""):
    n = nombre.strip().title()
    a1 = apellido.strip().title()
    a2 = apellido2.strip().title()
    
    apellidos = f"{a1} {a2}".strip()
    return f"Bienvenido {n} {apellidos}"

print(bienvenida(" nicolás ", "cano "))

# Opción con validación de datos, manejo de espacios y apellido2 opcional

def bienvenida(nombre: str, apellido: str, apellido2: str = "") -> str:
    for dato in [nombre, apellido]:
        if not dato or not isinstance(dato, str):
            return "Error: Los datos deben ser texto válido."
            
    return f"Bienvenido {nombre.title()} {apellido.title()} {apellido2.title()}".strip()

# Opcion con validación de datos, manejo de espacios y apellido2 opcional, con función para obtener datos
def obtener_dato(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isalpha():
            return valor.title()
        print("Por favor, ingresa un nombre válido (solo letras).")


nombre = obtener_dato("Ingresa tu nombre: ")
apellido = obtener_dato("Ingresa tu apellido: ")
apellido2 = input("Ingresa tu segundo apellido (opcional): ").strip().title()

print(f"Bienvenido {nombre} {apellido} {apellido2}")