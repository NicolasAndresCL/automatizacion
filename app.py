import pyautogui
import time
import random

# Configuración de seguridad: Si mueves el mouse a una esquina de la pantalla, el script se detiene.
pyautogui.FAILSAFE = True

def mantener_sesion_activa(intervalo_segundos=30):
    print("--- Simulador de Actividad Iniciado ---")
    print("Mueve el mouse a cualquier esquina de la pantalla para forzar la detención.")
    print("Presiona CTRL + C en la terminal para salir.")
    
    try:
        while True:
            # 1. Movimiento de mouse más "humano" (no vuelve al mismo punto exacto de inmediato)
            x_random = random.randint(-50, 50)
            y_random = random.randint(-50, 50)
            
            # Movemos el mouse con una duración pequeña para que el sistema vea desplazamiento real
            pyautogui.moveRel(x_random, y_random, duration=0.2)
            
            # 2. Presionar una tecla "muerta" (Shift es ideal porque no escribe nada)
            # Esto es mucho más efectivo para evitar que la pantalla se oscurezca
            pyautogui.press('shift')
            
            # 3. Informar en consola
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Actividad simulada (Mouse + Tecla Shift)")
            
            # Esperar el intervalo
            time.sleep(intervalo_segundos)
            
    except KeyboardInterrupt:
        print("\n[!] Script detenido por el usuario.")
    except Exception as e:
        print(f"\n[!] Error inesperado: {e}")

if __name__ == "__main__":
    # Si tu laptop se bloquea muy rápido, usa 15 o 20 segundos.
    mantener_sesion_activa(intervalo_segundos=20)