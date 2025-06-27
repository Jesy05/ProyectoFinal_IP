# Autor: Jesy Nicole González Jarquín
# Versión: 1.0
# Descripción: Menú principal del sistema UAM-CodeX - con estructura modular

import os

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrarMenu():
    print("📖" * 23)
    print("📚 UAM-CodeX — Plataforma Académica de Consola")
    print("📖" * 23)
    print("1️⃣  Ingresar como Publicador")
    print("2️⃣  Ingresar como Gestor")
    print("3️⃣  Ingresar como Lector")
    print("4️⃣  Salir") 
    print("🌀" * 23)

def main():
    while True:
        limpiarPantalla() 
        mostrarMenu()
        opcion = input("👉 Selecciona una opción (1-4): ")

        if opcion == "1":
            # --- Aquí se llamará a la función del módulo publicador ---
            # Ejemplo futuro: publicador.menuPublicador()
            print("\n✍️ Entrando como Publicador...")
            print("🔧 [placeholder] Esta función será implementada por el módulo publicador.py")
            input("\n⏎ Presiona Enter para volver al menú...")

        elif opcion == "2":
            # --- Aquí se llamará a la función del módulo revisor ---
            # Ejemplo futuro: revisor.menuRevisor()
            print("\n✅ Entrando como Gestor...")
            print("🔧 [placeholder] Esta función será implementada por el módulo gestor.py")

            # --- Aquí se llamará tambien a la función que muestra estadísticas del sistema que se quedan disponibles solo para el revisor ---
            # Ejemplo futuro: gestor.mostrarEstadisticas()
            print("\n📊 Estadísticas del sistema...")
            print("[Aca podría ver un resumen de las estadísticas del sistema, como número de publicaciones, revisiones pendientes, etc.]")
            print("🔧 [placeholder] Esta función será implementada por el módulo gestor.py")
            input("\n⏎ Presiona Enter para volver al menú...")

        elif opcion == "3":
            # --- Aquí se llamará a la función del módulo lector ---
            # Ejemplo futuro: lector.menuLector()
            print("\n📖 Entrando como Lector...")
            print("🔧 [placeholder] Esta función será implementada por el módulo lector.py")
            input("\n⏎ Presiona Enter para volver al menú...")

        elif opcion == "4":
            print("\n👋 ¡Gracias por usar UAM-CodeX! Hasta pronto.")
            break

        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo.")
            input("\n⏎ Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
