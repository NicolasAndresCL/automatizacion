import pyautogui
import time
import random
import sys

# Configuración de seguridad: Mover el mouse a una esquina detiene pyautogui
pyautogui.FAILSAFE = True

def inicializar_mouse():
    """Posiciona el mouse en el centro de la pantalla al iniciar."""
    ancho, alto = pyautogui.size()
    centro_x = ancho // 2
    centro_y = alto // 2
    
    print(f"\n📐 Dimensiones de pantalla: {ancho}x{alto}")
    print(f"📍 Posicionando mouse en centro: ({centro_x}, {centro_y})")
    
    pyautogui.moveTo(centro_x, centro_y, duration=0.5)
    time.sleep(1)

def mantener_sesion_activa(intervalo_segundos=5):
    """Mueve el mouse y presiona Shift para evitar el bloqueo de pantalla."""
    print("\n--- [MODO] Simulador de Actividad Iniciado ---")
    print("Presiona CTRL + C para volver al menú.")
    
    # Inicializar mouse en el centro
    inicializar_mouse()
    
    # Obtener dimensiones de pantalla una sola vez
    ancho, alto = pyautogui.size()
    
    # Definir márgenes seguros (píxeles de distancia desde los bordes)
    margen = 150
    
    # Calcular área segura donde el mouse se puede mover
    x_min = margen
    x_max = ancho - margen
    y_min = margen
    y_max = alto - margen
    
    print(f"🔒 Área segura: X({x_min}-{x_max}) Y({y_min}-{y_max})")
    
    try:
        while True:
            # Obtener posición actual del mouse
            x_actual, y_actual = pyautogui.position()
            
            # PARA FORZAR EL ERROR (comentado):
            # Descomenta las siguientes 2 líneas para generar movimientos hacia las esquinas
            # x_random = random.randint(-500, 500)
            # y_random = random.randint(-500, 500)
            
            # Movimiento aleatorio relativo pequeño (±40 píxeles)
            x_random = random.randint(-40, 40)
            y_random = random.randint(-40, 40)
            
            # Calcular nueva posición
            x_nueva = x_actual + x_random
            y_nueva = y_actual + y_random
            
            # SOLUCIÓN: Limitar SIEMPRE dentro del área segura (nunca toca bordes)
            x_nueva = max(x_min, min(x_nueva, x_max))
            y_nueva = max(y_min, min(y_nueva, y_max))
            
            # Mover a la posición limitada
            pyautogui.moveTo(x_nueva, y_nueva, duration=0.2)
            
            # Tecla Shift para mantener el sistema despierto
            pyautogui.press('shift')
            
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Actividad simulada (Mouse + Shift) | Posición: ({x_nueva}, {y_nueva})")
            
            time.sleep(intervalo_segundos)
    except KeyboardInterrupt:
        print("\n[!] Función detenida. Volviendo al menú...")
    except pyautogui.FailSafeException:
        print("\n[!] ⚠️ ¡Error de Fail-Safe detectado! El mouse tocó una esquina.")
        print("[!] Volviendo al menú...")

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