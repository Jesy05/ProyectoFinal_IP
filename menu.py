# main.py – GUI con expander de login y placeholders
# Versión: 1.1 GUI

import streamlit as st
from clases.classArticulo import Articulo
from modulos.modArticulo import menu_publicador
from modulos.modGestor import menu_gestor
from modulos.modLector import menu_lector 

from clases.classUsuario import Usuario
from clases.classRol import Rol
from clases.classGestor import GestorPermiso

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

# aca las validaciones de usuario, contraseña y rol
with st.expander("🔑 Iniciar sesión (elige tu rol)"):
    st.write("Por favor ingresa tus credenciales")

    usuario_input = st.text_input("Usuario", key="usuario_input")
    contra_input = st.text_input("Contraseña", type="password", key="contra_input")

    # Guardar el rol seleccionado en session_state
    if "rol_seleccionado" not in st.session_state:
        st.session_state["rol_seleccionado"] = ""

    rol = st.selectbox(
        "Rol:",
        ("", "Publicador", "Gestor", "Lector"),
        index=0,
        key="rol_dropdown"
    )

    st.session_state["rol_seleccionado"] = rol

    # Mostrar campo adicional si elige Gestor
    clave_gestor = ""
    if rol == "Gestor":
        clave_gestor = st.text_input("🔐 Clave de Gestor", type="password", key="clave_gestor")

    if st.button("Iniciar sesión"):
        usuario = Usuario(usuario_input, contra_input)
        rol_usuario = Rol(rol)

        if not usuario.validar_usuario():
            st.error("❌ Usuario inválido (máx 50 caracteres, letras, números, guiones bajos o espacios)")
        elif not usuario.validar_contrasena():
            st.error("❌ Contraseña inválida (12–20 caracteres, debe incluir al menos un símbolo especial)")
        elif not rol_usuario.validar_rol():
            st.error("❌ Rol inválido.")
        elif rol == "Gestor":
            permiso = GestorPermiso(clave_gestor)
            if not permiso.validar_pass():
                st.error("❌ Clave de Gestor inválida o no autorizada.")
            else:
                st.success("✅ Sesión iniciada como Gestor")
                st.session_state["rol"] = "✅ Gestor"
        else:
            icon = "✍️" if rol == "Publicador" else "📖"
            st.success(f"✅ Sesión iniciada como {rol}")
            st.session_state["rol"] = f"{icon} {rol}"


# ─── Mostrar contenido primera ver con los roles ────────────
rol_actual = st.session_state["rol"]

if rol_actual: # Verificamos si hay un rol seleccionado
    st.success(f"Has iniciado sesión como **{rol_actual.split()[1]}**")

    if rol_actual == "✍️ Publicador":
        st.header("Panel de Publicador")
        menu_publicador()

    elif rol_actual == "✅ Gestor":
         st.header("Panel de Gestor")
         menu_gestor()

    elif rol_actual == "📖 Lector":
         st.header("Panel de Lector")
         menu_lector()

    # ── Tarjetas de 3 artículos de muestra ─────────────
    st.subheader("Artículos destacados")
    col1,= st.columns(1)
    for col, n in zip((col1,), (1,)): #zip es usado para iterar sobre columnas y números aca
        with col:
            st.markdown(
                f"### 📄 GitHub 👾 #{n}\n"
                "_Tutorial Para GitHub_\n"
                "\nEste tutorial te enseña lo esencial de GitHub, como los repositorios,"
                " ramas y pull requests. Ideal para principiantes.\n\n"
            )

    col1,= st.columns(1)
    for col, n in zip((col1,), (1,)): #zip es usado para iterar sobre columnas y números aca
        with col:
            st.markdown(
                f"### 📄 Visual Studio Code 🐢 #{n}\n"
                "_Tutorial Para VS_\n"
                "\nGuía rápida para usar Visual Studio Code"
            )        
else:
    st.warning("Selecciona un rol en el expander para continuar.")
