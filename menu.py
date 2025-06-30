# main.py – GUI con expander de login y placeholders
# Autor: Jesy Nicole González Jarquín
# Versión: 1.1 GUI

import streamlit as st

# ─── Importaciones futuras ─────────────────────────────
# from modulos.publicador import menu_publicador
# from modulos.gestor     import menu_gestor
# from modulos.lector     import menu_lector
# ───────────────────────────────────────────────────────

st.set_page_config(page_title="UAM‑CodeX", page_icon="📚")

# ─── Sidebar ───────────────────────────────────────────
side = st.sidebar.radio("Menú", ("ℹ️ Acerca", "❓ Ayuda"))

if side == "ℹ️ Acerca":
    st.sidebar.markdown(
        "**UAM‑CodeX** es una plataforma académica colaborativa "
        "desarrollada por estudiantes de Ingeniería en Sistemas para "
        "compartir artículos, tutoriales y proyectos."
    )
elif side == "❓ Ayuda":
    st.sidebar.markdown(
        "Para soporte, contacta:\n\n"
        "- Marian Alejandra Guillén Castillo\n"
        "- Nora María Obregón Membreño\n"
        "- Jesy Nicole González Jarquín\n\n"
        "📧  **UAM‑CodeX@uamv.edu.ni**"
    )

# ─── Landing page ──────────────────────────────────────
st.title("📚 UAM‑CodeX")
st.markdown(
    "Bienvenido a la plataforma donde estudiantes comparten conocimiento "
    "y aprenden de las experiencias de sus compañeros."
)

# Guardamos el rol en session_state
if "rol" not in st.session_state:
    st.session_state["rol"] = ""

with st.expander("🔑 Iniciar sesión (elige tu rol)"):
    rol = st.selectbox(
        "Rol:",
        ("", "✍️ Publicador", "✅ Gestor", "📖 Lector"),
        index=0,
        key="rol_select"
    )
    if rol:
        st.session_state["rol"] = rol

# ─── Mostrar contenido solo cuando haya rol ────────────
rol_actual = st.session_state["rol"]

if rol_actual:
    st.success(f"Has iniciado sesión como **{rol_actual.split()[1]}**")

    if rol_actual == "✍️ Publicador":
        st.header("Panel de Publicador")
        # menu_publicador()
        st.info("🔧 Placeholder → aquí irá `menu_publicador()`")

    elif rol_actual == "✅ Gestor":
        st.header("Panel de Gestor")
        # menu_gestor()
        st.info("🔧 Placeholder → aquí irá `menu_gestor()`")
        st.subheader("📊 Estadísticas (placeholder)")
        st.write("Total artículos: 0 · Pendientes: 0 · Aprobados: 0")

    elif rol_actual == "📖 Lector":
        st.header("Panel de Lector")
        # menu_lector()
        st.info("🔧 Placeholder → aquí irá `menu_lector()`")

    # ── Tarjetas de 3 artículos de muestra ─────────────
    st.subheader("Artículos destacados")
    col1, col2, col3 = st.columns(3)
    for col, n in zip((col1, col2, col3), (1, 2, 3)):
        with col:
            st.markdown(
                f"### 📄 Artículo #{n}\n"
                "_Resumen de prueba..._\n"
                "🔧 **En construcción**"
            )
else:
    st.warning("Selecciona un rol en el expander para continuar.")
