# modulos/modPublicador.py

import streamlit as st
from clases.classArticulo import Articulo

articulos_borrador = []

def menu_publicador():
    st.subheader("📝 Crear nuevo artículo")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    contenido = st.text_area("Contenido")

    if st.button("Guardar borrador"):
        nuevo = Articulo(titulo, autor, contenido)
        articulos_borrador.append(nuevo)
        st.success("Artículo guardado en borradores.")

    if articulos_borrador:
        st.subheader("📋 Borradores guardados")
        for i, art in enumerate(articulos_borrador):
            st.markdown(f"**{i+1}. {art.titulo}** – _{art.autor}_")
            if st.button(f"📝 Editar {art.titulo}", key=f"edit{i}"):
                editar_articulo(i)

def editar_articulo(idx):
    art = articulos_borrador[idx]
    st.subheader(f"📝 Editando: {art.titulo}")
    art.titulo = st.text_input("Nuevo título", value=art.titulo)
    art.autor = st.text_input("Nuevo autor", value=art.autor)
    art.contenido = st.text_area("Nuevo contenido", value=art.contenido)
    st.success("Cambios guardados en borrador.")
