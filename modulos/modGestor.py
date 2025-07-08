# modulos/modGestor.py

import streamlit as st

articulos_aprobados = [] # Lista para almacenar artículos aprobados 

def menu_gestor():
    st.subheader("📤 Artículos en revisión")
    usuarios = st.session_state.get("usuarios_registrados", [])
    hay_borradores = False

    for user in usuarios:
        if user.rol == "Publicador":
            for i, art in enumerate(user.borradores):
                hay_borradores = True
                with st.expander(f"{user.nombre} – {art.titulo}"):
                    st.write(f"Autor: {art.autor}")
                    st.write(art.contenido)

                    col1, col2 = st.columns(2)
                    if col1.button("✅ Aprobar", key=f"aprobar_{user.nombre}_{i}"):
                        articulos_aprobados.append(art)
                        user.borradores.pop(i)
                        st.success("Artículo aprobado.")
                        st.rerun()

                    if col2.button("❌ Rechazar", key=f"rechazar_{user.nombre}_{i}"):
                        user.borradores.pop(i)
                        st.warning("Artículo rechazado.")
                        st.rerun()

    if not hay_borradores:
        st.info("No hay artículos en revisión por el momento.")

# --- Nueva sección: Eliminar usuarios ---
    st.markdown("---")
    st.subheader("🔒 Administración de usuarios")
    st.write("Seleccione un usuario para poderlo eliminarlo del sistema.")

    nombres_disponibles = [u.nombre for u in usuarios if u.rol != "Gestor"]
    if nombres_disponibles:
        nombre_a_eliminar = st.selectbox("Usuario a eliminar:", nombres_disponibles)

        confirmar = st.checkbox("Confirmo que deseo eliminar a este usuario permanentemente.")
        if st.button("🗑️ Eliminar usuario"):
            if confirmar:
                for i, u in enumerate(usuarios):
                    if u.nombre == nombre_a_eliminar:
                        usuarios.pop(i)
                        st.success(f"✅ Usuario '{nombre_a_eliminar}' eliminado correctamente.")
                        st.rerun()
            else:
                st.warning("Debes confirmar la eliminación.")
    else:
        st.info("No hay usuarios disponibles para eliminar.")