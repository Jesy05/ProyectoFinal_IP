# main.py –

import streamlit as st
import os
from modulos.modPublicador import menu_publicador
from modulos.modGestor import menu_gestor
from modulos.modLector import menu_lector 

from clases.classArticulo import Articulo
from clases.classUsuario import Usuario
from clases.classRol import Rol
from clases.classGestor import GestorPermiso

st.set_page_config(page_title="UAM‑CodeX", page_icon="📚")

# ─── ZONA GLOBAL ─────────────────────────────────────────
if "usuarios_registrados" not in st.session_state:
    st.session_state["usuarios_registrados"] = []
#con el session_state podemos guardar datos entre recargas de la página
#esto es útil para mantener el estado de la aplicación mientras no se cierre el navegador
# esto porque no tenemos una base de datos real real
usuarios_registrados = st.session_state["usuarios_registrados"]   # esta area es para que no se vuelvan inalcanzables las cosas de este tipo
#esto es un tipo de base de datos temporal y no muy escalable

# ─────────────────────────────────────────────────────────


# _____ Mostrar banner principal __________________________
ruta_banner = os.path.join("static", "banner_inicio.png")
if os.path.exists(ruta_banner):
    st.image(ruta_banner, use_container_width=True)


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


#__________ expander ____________________

# aca las validaciones de usuario, contraseña y rol <<<< 
with st.expander("🔑 Iniciar sesión/ Registrarse (elige tu rol)"):
    st.write("Por favor ingresa tus credenciales")

    usuario_input = st.text_input("Usuario", key="usuario_input")
    # Recordar contraseña si ya existe
    if "contrasena_recordada" not in st.session_state:
            st.session_state["contrasena_recordada"] = ""

    # Campo de contraseña
    contra_input = st.text_input(
        "Contraseña", 
        type="password", 
        key="contra_input", 
        value=st.session_state["contrasena_recordada"]
    )

    # Botón recordar contraseña
    if st.button("🔓 Recordar contraseña"):
        recordado = next((u for u in usuarios_registrados if u.nombre == usuario_input), None)
        if recordado:
            st.session_state["contrasena_recordada"] = recordado.contra
            st.success("Contraseña recuperada.")
            st.rerun()
        else:
            st.warning("Usuario no encontrado.")


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

    rol_actual = st.session_state.get("rol", "")

    # verificacion extra para que no llame a split cuando no tiene que 
    if rol_actual:
        partes = rol_actual.split()
         # Si viene con icono + espacio + rol (p.ej. "✍️ Publicador"), tendrá al menos 2 items
        rol_mostrar = partes[1] if len(partes) > 1 else partes[0]
        st.success(f"Has iniciado sesión como **{rol_mostrar}**")
        # ... resto de paneles
    else:
         st.warning("Selecciona un rol en el expander para continuar.")

    # Mostrar campo adicional si elige Gestor
    clave_gestor = ""
    if rol == "Gestor":
        clave_gestor = st.text_input("🔐 Clave de Gestor", type="password", key="clave_gestor")
    
    #weeeeeeeeeeeee

    if st.button("Iniciar Sesión/ Registrarse"):
        existente = next((u for u in usuarios_registrados if u.nombre == usuario_input), None)

        if existente:
            # Intentar iniciar sesión
            if existente.contra != contra_input:
                st.error("❌ Contraseña incorrecta para este usuario.")
            elif existente.rol != rol:
                st.error("❌ El rol seleccionado no coincide con el del usuario registrado.")
            else:
                st.session_state["usuario_actual"] = existente
                icon = "✍️" if rol == "Publicador" else "📖" if rol == "Lector" else "✅"
                st.session_state["rol"] = f"{icon} {rol}"
                st.success(f"✅ Bienvenido de nuevo, {usuario_input} ({rol}).")
        else:
            # Crear nuevo usuario
            nuevo_usuario = Usuario(usuario_input, contra_input if contra_input is not None else "", rol)

            if not nuevo_usuario.validar_usuario():
                st.error("❌ Usuario inválido…")
            elif not nuevo_usuario.validar_contrasena():
                st.error("❌ Contraseña inválida…")
            elif not Rol(rol).validar_rol():
                st.error("❌ Rol inválido.")
            elif rol == "Gestor":
                permiso = GestorPermiso(clave_gestor)
                if not permiso.validar_pass():
                    st.error("❌ Clave de Gestor inválida o no autorizada.")
                else:
                    usuarios_registrados.append(nuevo_usuario)
                    st.session_state["usuario_actual"] = nuevo_usuario
                    st.session_state["rol"] = "✅ Gestor"
                    st.success("✅ Cuenta de Gestor creada/ Sesión iniciada.")
            else:
                usuarios_registrados.append(nuevo_usuario)
                st.session_state["usuario_actual"] = nuevo_usuario
                icon = "✍️" if rol == "Publicador" else "📖"
                st.session_state["rol"] = f"{icon} {rol}"
                st.success(f"✅ Cuenta de {rol} creada/ Sesión iniciada.")



  #weeee

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
   
  # 🔒 Botón para cerrar sesión
    if st.button("🔒 Cerrar sesión"):
        claves_preservar = ["usuarios_registrados"]
        # Limpia todo lo que quede en session_state
        for k in list(st.session_state.keys()):
            if k not in claves_preservar:
                del st.session_state[k]
        # Opcional: volver a cargar la página
        st.rerun()


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
        st.write("Visual Studio Code")      
