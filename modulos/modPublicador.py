# modulos/modPublicador.py

import streamlit as st
from clases.classArticulo import Articulo


def menu_publicador():
    st.subheader("📝 Crear nuevo artículo")
    usuario_actual = st.session_state.get("usuario_actual")
    if not usuario_actual:
        st.warning("No se encontró la sesión del usuario.")
        return
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    contenido = st.text_area("Contenido")


    if st.button("Guardar borrador"):
        nuevo = Articulo(titulo, usuario_actual.nombre, contenido)
        usuario_actual.agregar_borrador(nuevo)
        st.success("Artículo guardado en borradores.")

    if usuario_actual.borradores:
        st.subheader("📋 Tus borradores guardados")
        for i, art in enumerate(usuario_actual.borradores):
            st.markdown(f"**{i+1}. {art.titulo}** – _{art.autor}_")
            if st.button(f"📝 Editar {art.titulo}", key=f"edit{i}"):
                editar_articulo(usuario_actual, i)

def editar_articulo(usuario_actual, i):
    art = usuario_actual.borradores[i]
    st.subheader(f"📝 Editando: {art.titulo}")

    # claves únicas por artículo
    k_t = f"titulo_{i}"
    k_a = f"autor_{i}"
    k_c = f"contenido_{i}"
    k_guardado = f"guardado_{i}"

    nuevo_titulo = st.text_input("Nuevo título", value=art.titulo, key=f"titulo_{i}")
    nuevo_autor = st.text_input("Nuevo autor", value=art.autor, key=f"autor_{i}")
    nuevo_contenido = st.text_area("Nuevo contenido", value=art.contenido, key=f"contenido_{i}")

    # Guardar solo si hay cambios
    if st.button("💾 Guardar cambios", key=f"guardar_{i}"):
        hubo_cambios = (
            nuevo_titulo != art.titulo or
            nuevo_autor != art.autor or
            nuevo_contenido != art.contenido
        )
        if hubo_cambios:
            art.titulo = nuevo_titulo
            art.autor = nuevo_autor
            art.contenido = nuevo_contenido
            st.session_state[k_guardado] = True
        else:
            st.session_state[k_guardado] = False

    if st.session_state.get(k_guardado) is True:
        st.success("✅ Cambios guardados en borrador.")
    elif st.session_state.get(k_guardado) is False:
        st.info("ℹ️ No hubo cambios por guardar.")