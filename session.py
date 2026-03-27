import time
from playwright.sync_api import sync_playwright

def capturar_sesion_sence():
    with sync_playwright() as p:
        # Usamos un navegador visible para el login
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Navegando a SENCE...")
        page.goto("https://auladigital.sence.cl/login/index.php")
        
        print("\nPASOS A SEGUIR:")
        print("1. Ingresa tu RUT en la primera pantalla.")
        print("2. Haz clic en 'Acceder'.")
        print("3. Cuando te redirija a ClaveÚnica, ingresa tu RUT y Clave.")
        print("4. Una vez que estés DENTRO de tu aula virtual (viendo tus cursos), vuelve aquí.")

        # Esperamos a que el usuario termine el proceso manualmente
        input("\n--> Presiona ENTER en esta terminal CUANDO YA ESTÉS LOGUEADO en el Aula Virtual...")

        # Guardamos el estado (Cookies, Tokens, Sesiones de ClaveÚnica)
        context.storage_state(path="sesion_sence.json")
        print("\n¡Éxito! Sesión guardada en 'sesion_sence.json'")
        
        browser.close()

if __name__ == "__main__":
    capturar_sesion_sence()