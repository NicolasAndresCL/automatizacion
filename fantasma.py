import time
import random
from playwright.sync_api import sync_playwright

def mantener_sence_activo(min_m=20, max_m=30):
    print("--- Iniciando Mantenedor de Sesión SENCE (Modo Invisible) ---")
    
    with sync_playwright() as p:
        # Cargamos el navegador invisible
        browser = p.chromium.launch(headless=True)
        
        try:
            # Cargamos la sesión que guardamos antes
            context = browser.new_context(storage_state="sesion_sence.json")
            page = context.new_page()

            # Vamos directo al aula digital
            print(f"[{time.strftime('%H:%M:%S')}] Accediendo al Aula Digital...")
            page.goto("https://auladigital.sence.cl/")
            
            # Verificamos si entramos bien (opcional)
            print(f"[{time.strftime('%H:%M:%S')}] Título actual: {page.title()}")

            while True:
                # Intervalo aleatorio (20 a 30 minutos)
                intervalo = random.randint(min_m * 60, max_m * 60)
                print(f"[{time.strftime('%H:%M:%S')}] Esperando {intervalo/60:.1f} min para refrescar...")
                
                time.sleep(intervalo)

                # En lugar de atrás/adelante, refrescamos o navegamos al inicio
                # Esto es más robusto para ClaveÚnica
                page.reload()
                print(f"[{time.strftime('%H:%M:%S')}] ↑ Página refrescada (Sesión mantenida)")
                
                # Opcional: Pequeño movimiento aleatorio dentro de la página "invisible"
                page.mouse.wheel(0, 500)
                time.sleep(2)
                page.mouse.wheel(0, -500)

        except Exception as e:
            print(f"\n[!] Error: {e}")
            print("Es posible que la sesión haya expirado. Ejecuta el Paso 1 de nuevo.")
        finally:
            browser.close()

if __name__ == "__main__":
    mantener_sence_activo()