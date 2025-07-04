# modulos/modGestor.py

import streamlit as st
from modulos.modArticulo import articulos_borrador

articulos_aprobados = []

def menu_gestor():
    st.subheader("📤 Artículos en revisión")
    for i, art in enumerate(articulos_borrador):
        with st.expander(f"{i+1}. {art.titulo}"):
            st.write(f"Autor: {art.autor}")
            st.write(art.contenido)
            col1, col2 = st.columns(2)
            if col1.button("✅ Aprobar", key=f"aprobar{i}"):
                articulos_aprobados.append(art)
                articulos_borrador.pop(i)
                st.success("Artículo aprobado.")
                st.rerun()
            if col2.button("❌ Rechazar", key=f"rechazar{i}"):
                articulos_borrador.pop(i)
                st.warning("Artículo rechazado.")
                st.rerun()
