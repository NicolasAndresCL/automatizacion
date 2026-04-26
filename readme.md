# 🤖 AutoSession — Simulador de Actividad de Escritorio

Script en Python para mantener una sesión activa y automatizar navegación básica en el navegador, evitando bloqueos de pantalla o cierres de sesión por inactividad.

---

## 📋 Descripción

**AutoSession** es una herramienta de automatización de escritorio liviana que ofrece dos modos de operación:

- **Modo 1 – Mantener sesión activa:** Mueve el mouse aleatoriamente y presiona `Shift` a intervalos regulares para simular actividad y evitar que el sistema se bloquee.
- **Modo 2 – Navegación automática:** Alterna entre "Atrás" y "Adelante" en una pestaña específica del navegador a intervalos aleatorios.

---

## ⚙️ Requisitos

- Python 3.7+
- [`pyautogui`](https://pyautogui.readthedocs.io/)

### Instalación de dependencias

```bash
pip install pyautogui
```

---

## 🚀 Uso

```bash
python autosession.py
```

Al ejecutar, se mostrará el menú principal:
===============================
```

MENU DE AUTOMATIZACIÓN

Mantener sesión activa (Mouse/Teclado)
Navegación automática (Atrás/Adelante)
Salir
```


### Modo 1 – Mantener sesión activa
```

Mueve el mouse en un rango aleatorio de ±50 px y presiona `Shift` cada **5 segundos** (configurable).
Actividad simulada (Mouse + Shift)
Actividad simulada (Mouse + Shift)
```

### Modo 2 – Navegación automática
```

Solicita el número de pestaña (1–9) y alterna entre `Alt+Left` y `Alt+Right` en intervalos de entre 5 y 10 segundos.
 ← Atrás
 → Adelante
```

---

## 🛑 Cómo detener el script
```
| Acción | Resultado |
|---|---|
| `CTRL + C` | Vuelve al menú principal |
| Mover el mouse a cualquier esquina | Detiene `pyautogui` (FAILSAFE) |
| Opción `3` en el menú | Cierra el programa |
```

---

## 🔧 Configuración

Puedes ajustar los parámetros directamente en el código:

| Parámetro | Ubicación | Valor por defecto | Descripción |
|---|---|---|---|
| `intervalo_segundos` | `mantener_sesion_activa()` | `5` | Segundos entre cada simulación de actividad |
| `intervalo` (navegación) | `ejecutar_navegacion_automatica()` | `5–10 s` | Rango de espera entre navegaciones |

> 💡 Para simular pausas más largas (ej. 20–30 min), cambia `random.randint(5, 10)` por `random.randint(1200, 1800)`.

---

## ⚠️ Aviso

Este script está pensado para uso personal en entornos donde el usuario es el propietario del equipo. Úsalo de forma responsable y respetando las políticas de la plataforma o entorno donde se ejecute.

---

## 📁 Estructura
- app.py # Script mouse
- main.py # Script Adelante y Atras
- automatizador.py   # Script principal (ambos juntos)