# main.py – GUI inicial con Streamlit
# Autor: Jesy Nicole González Jarquín
# Versión: 1.0 GUI
# Descripción: Menú principal gráfico de UAM-CodeX

import streamlit as st

# ──────── IMPORTACIONES FUTURAS ──────────────────────────
# from modulos.publicador import menu_publicador
# from modulos.gestor     import menu_gestor          # incluye estadísticas
# from modulos.lector     import menu_lector
# ─────────────────────────────────────────────────────────

st.set_page_config(page_title="UAM-CodeX", page_icon="📚")

st.title("📚 UAM-CodeX — Plataforma Académica")

opcion = st.sidebar.radio(
    "Selecciona tu rol",
    ("🏠 Inicio",
     "✍️ Publicador",
     "✅ Gestor",
     "📖 Lector",
     "🚪 Salir")
)

# ──────── VISTAS ─────────────────────────────────────────
if opcion == "🏠 Inicio":
    st.success("Bienvenida/o. Elige un rol en la barra lateral ➡️")

elif opcion == "✍️ Publicador":
    st.header("✍️ Módulo Publicador")
    # menu_publicador()
    st.info("🔧 Placeholder → aquí se llamará a `menu_publicador()` del módulo *publicador.py*")

elif opcion == "✅ Gestor":
    st.header("✅ Módulo Gestor")
    # menu_gestor()
    st.info("🔧 Placeholder → aquí se llamará a `menu_gestor()` del módulo *gestor.py*")
    st.subheader("📊 Estadísticas del sistema")
    st.write("[Aquí se mostrará el resumen: artículos, revisiones, etc.]")

elif opcion == "📖 Lector":
    st.header("📖 Módulo Lector")
    # menu_lector()
    st.info("🔧 Placeholder → aquí se llamará a `menu_lector()` del módulo *lector.py*")

elif opcion == "🚪 Salir":
    st.warning("👋 ¡Gracias por usar UAM-CodeX!")
    st.stop()   # finaliza la app para esa sesión
