def generar_secuencia():
    continuar = True
    
    while continuar:
        print(f"\n------------ACT 1---------------") 
        num = int(input("Ingrese un número (2-100 para pares, 1-99 para impares): "))
        
        if num <= 0 or num > 100:
            print("No es posible realizarlo. Por favor, ingrese el número de nuevo.")
        
        else:
            continuar = False
            
            if num % 2 == 0:
                print("Usted ha ingresado un número par y los números pares siguientes son:")
                for i in range(num + 2, 101, 2):
                    print(i, end=" ")
                print()
                
            else:
                print("Usted ha ingresado un número impar y los números impares siguientes son:")
                for i in range(num + 2, 100, 2):
                    print(i, end=" ")
                print() 

generar_secuencia()

"""El Bucle while: Usamos una variable continuar = True. El programa solo se detiene cuando el número está dentro del rango (1-100), cambiando la variable a False.

Validación Manual: El if num <= 0 or num > 100 se encarga de filtrar los casos que pide tu ejercicio sin necesidad de herramientas complejas.

El parámetro end=" ": En la función print(), esto evita que cada número se imprima en una línea nueva, haciendo que aparezcan uno al lado del otro con un espacio, tal como en tus capturas de pantalla."""


def gestionar_notas():
    notas = []
    
    for i in range(5):
        while True:
            nota = float(input(f"Ingrese la nota {i+1} (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota fuera de rango. Debe ser entre 0 y 10.")

    media = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)

    print(f"\n------------ACT 2---------------") 
    print("--- Resultados del Alumno ---")
    print(f"Todas las notas: {notas}")
    print(f"Nota media: {media:.2f}")
    print(f"Nota más alta: {maxima}")
    print(f"Nota más baja: {minima}")

gestionar_notas()


def consultar_mes():
    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:
        num_mes = int(input("Ingrese el número de un mes (1-12): "))
        
        if 1 <= num_mes <= 12:
            indice = num_mes - 1
            
            nombre = nombres_meses[indice]
            dias = dias_meses[indice]
            print(f"\n------------ACT 3---------------") 
            print(f"El mes es {nombre} y tiene {dias} días.")
            break
        else:
            print("Número de mes inválido. Intente de nuevo.")

consultar_mes()