def generar_secuencia():
    continuar = True
    
    while continuar:
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