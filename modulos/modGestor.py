# modulos/modGestor.py

import streamlit as st
from modulos.modArticulo import articulos_borrador

articulos_aprobados = [] # Lista para almacenar artículos aprobados 

def menu_gestor():
    st.subheader("📤 Artículos en revisión")
    for i, art in enumerate(articulos_borrador): # Iteramos sobre los artículos en borrador
        with st.expander(f"{i+1}. {art.titulo}"): # Usamos expander para mostrar cada artículo
            st.write(f"Autor: {art.autor}") # Mostramos el autor del artículo
            st.write(art.contenido) 
            col1, col2 = st.columns(2) # Creamos dos columnas para mostrar la información
            if col1.button("✅ Aprobar", key=f"aprobar{i}"):
                articulos_aprobados.append(art)
                articulos_borrador.pop(i)
                st.success("Artículo aprobado.")
                st.rerun()
            if col2.button("❌ Rechazar", key=f"rechazar{i}"):
                articulos_borrador.pop(i)
                st.warning("Artículo rechazado.")
                st.rerun()
