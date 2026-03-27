import random
import pyautogui
import time

def ejecutar_navegacion_automatica(num_pestana=1, min_intervalo=1200, max_intervalo=1800):
    """
    Realiza una acción de navegación (atrás/adelante) en una pestaña específica
    dentro de un intervalo de tiempo aleatorio.
    """
    print(f"Script activo en la pestaña {num_pestana}. Presiona CTRL + C para detener.")
    
    try:
        while True:
            # Calculamos tiempos aleatorios en cada ciclo para mayor variabilidad
            intervalo = random.randint(min_intervalo, max_intervalo)
            espera_entre_paginas = random.randint(4, 8)

            time.sleep(intervalo)

            # Ir a la pestaña específica (Ctrl + número)
            pyautogui.hotkey('ctrl', str(num_pestana))
            time.sleep(1)

            # Acción: Atrás
            pyautogui.hotkey('alt', 'left')
            print(f"[{time.strftime('%H:%M:%S')}] ← Página anterior")

            time.sleep(espera_entre_paginas)

            # Acción: Adelante
            pyautogui.hotkey('alt', 'right')
            print(f"[{time.strftime('%H:%M:%S')}] → Página siguiente")
            
    except KeyboardInterrupt:
        print("\nScript detenido por el usuario.")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Puedes cambiar los valores aquí al llamar a la función
    ejecutar_navegacion_automatica(num_pestana=1, min_intervalo=1200, max_intervalo=1800)