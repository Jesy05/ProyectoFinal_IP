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
