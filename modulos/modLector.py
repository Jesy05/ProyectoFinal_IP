# modulos/modLector.py

import streamlit as st
from modulos.modGestor import articulos_aprobados

def menu_lector():
    st.subheader("📖 Artículos disponibles")# Enseña articulos disponibles para el lector y oculta los que estan en borrador
    if not articulos_aprobados:
        st.info("No hay artículos recientes aún.")
    for i, art in enumerate(articulos_aprobados):
        with st.expander(f"{i+1}. {art.titulo} – {art.autor}"):
            st.markdown(f"**Resumen:**\n{art.contenido[:150]}...")
            if st.button("🔍 Ver más", key=f"ver{i}"):
                st.write(art.contenido)
