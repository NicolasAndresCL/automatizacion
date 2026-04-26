import pyautogui
import time
import random
import sys

# Configuración de seguridad: Mover el mouse a una esquina detiene pyautogui
pyautogui.FAILSAFE = True

def mantener_sesion_activa(intervalo_segundos=5):
    """Mueve el mouse y presiona Shift para evitar el bloqueo de pantalla."""
    print("\n--- [MODO] Simulador de Actividad Iniciado ---")
    print("Mueve el mouse a cualquier esquina para forzar la detención.")
    print("Presiona CTRL + C para volver al menú.")
    
    try:
        while True:
            # Movimiento aleatorio relativo
            x_random = random.randint(-50, 50)
            y_random = random.randint(-50, 50)
            pyautogui.moveRel(x_random, y_random, duration=0.2)
            
            # Tecla Shift para mantener el sistema despierto
            pyautogui.press('shift')
            
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Actividad simulada (Mouse + Shift)")
            
            time.sleep(intervalo_segundos)
    except KeyboardInterrupt:
        print("\n[!] Función detenida. Volviendo al menú...")

def ejecutar_navegacion_automatica():
    """Navega atrás y adelante en una pestaña del navegador."""
    try:
        pestana = input("¿Qué número de pestaña quieres usar? (1-9): ")
        print(f"\n--- [MODO] Navegación Automática (Pestaña {pestana}) ---")
        print("Presiona CTRL + C para volver al menú.")
        
        while True:
            # Intervalos aleatorios (aquí ajustados a segundos cortos para prueba)
            # Puedes cambiarlos a 1200 y 1800 para los 20-30 min originales
            intervalo = random.randint(5, 10) 
            time.sleep(intervalo)

            # Ir a la pestaña específica
            pyautogui.hotkey('ctrl', str(pestana))
            time.sleep(1)

            # Acción: Atrás
            pyautogui.hotkey('alt', 'left')
            print(f"[{time.strftime('%H:%M:%S')}] ← Atrás")

            time.sleep(random.randint(2, 4))

            # Acción: Adelante
            pyautogui.hotkey('alt', 'right')
            print(f"[{time.strftime('%H:%M:%S')}] → Adelante")
            
    except KeyboardInterrupt:
        print("\n[!] Función detenida. Volviendo al menú...")

def menu_principal():
    """Muestra el menú de selección."""
    while True:
        print("\n===============================")
        print("      MENU DE AUTOMATIZACIÓN")
        print("===============================")
        print("1. Mantener sesión activa (Mouse/Teclado)")
        print("2. Navegación automática (Atrás/Adelante)")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mantener_sesion_activa()
        elif opcion == "2":
            ejecutar_navegacion_automatica()
        elif opcion == "3":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()