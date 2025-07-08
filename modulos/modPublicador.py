# modulos/modPublicador.py

import streamlit as st
from clases.classArticulo import Articulo


def menu_publicador():
    st.subheader("📝 Crear nuevo artículo") # Muestra un subtítulo más pequeño que un st.title
    # útil para secciones, al igual que da estructura al contenido.

    usuario_actual = st.session_state.get("usuario_actual") # Recupera datos guardados en la sesión y saber quién está logueado.
    # si no hay usuario logueado, muestra un mensaje de advertencia y sale de la función
    
    # como no hay una base de datos real se podrán borrar esos usuarios si se regarga la página
    # mientras esto no suceda se podrá volver a entrar sin problemas. 
    
    if not usuario_actual:
        st.warning("No se encontró la sesión del usuario.") #Muestra una alerta con mensaje de advertencia.
        # sucederá por errores leves, faltas de acceso, campos no llenados.
        return
    titulo = st.text_input("Título") # Muestra un campo de texto para ingresar el título del artículo.
    # st.text_input es un campo de texto de una sola línea.
    autor = st.text_input("Autor") # Muestra un campo de texto para ingresar el autor del artículo.
    # st.text_input es un campo de texto de una sola línea.
    contenido = st.text_area("Contenido")# Muestra un área de texto para ingresar el contenido del artículo.
    # st.text_area es un campo de texto de varias líneas o muy largo.


    if st.button("Guardar borrador"): # Muestra un botón para guardar el artículo como borrador.
        # st.button es un botón que al hacer clic ejecuta una acción.
        nuevo = Articulo(titulo, usuario_actual.nombre, contenido)
        usuario_actual.agregar_borrador(nuevo)
        st.success("Artículo guardado en borradores.") # Muestra un mensaje de éxito al guardar el artículo como borrador.
        # st.success es un mensaje de éxito que se muestra al usuario.

    if usuario_actual.borradores:
        st.subheader("📋 Tus borradores guardados") #
        for i, art in enumerate(usuario_actual.borradores):
            st.markdown(f"**{i+1}. {art.titulo}** – _{art.autor}_") # markdown sirve para mostrar texto con formato
            if st.button(f"📝 Editar {art.titulo}", key=f"edit{i}"): # Igual a st.button, pero key lo hace único por cada artículo, así Streamlit no los confunde.
                editar_articulo(usuario_actual, i)

def editar_articulo(usuario_actual, i):
    art = usuario_actual.borradores[i]
    st.subheader(f"📝 Editando: {art.titulo}")

    # claves únicas por artículo
    # Esto es importante para que Streamlit pueda identificar cada campo de entrada y botón de forma única.
    # Si no se usan claves únicas, Streamlit podría confundir los campos y botones entre sí, especialmente 
    # si hay varios artículos en la lista. 
    k_t = f"titulo_{i}" # Claves únicas para cada campo de entrada y botón.
    k_a = f"autor_{i}"
    k_c = f"contenido_{i}"
    k_guardado = f"guardado_{i}"

    nuevo_titulo = st.text_input("Nuevo título", value=art.titulo, key=f"titulo_{i}") # st.text_input carga un valor inicial (prellenado).
    # value=art.titulo carga el título actual del artículo para que el usuario pueda editarlo.
    # key=f"titulo_{i}" asegura que cada campo de texto tenga una clave única
    nuevo_autor = st.text_input("Nuevo autor", value=art.autor, key=f"autor_{i}")
    nuevo_contenido = st.text_area("Nuevo contenido", value=art.contenido, key=f"contenido_{i}") # multilinea.

    # Guardar solo si hay cambios
    if st.button("💾 Guardar cambios", key=f"guardar_{i}"):# Botón que guarda los cambios si el usuario modificó algo.
        #El key es clave para que Streamlit entienda que este botón es único para el artículo i.
        hubo_cambios = ( #Esta línea compara lo que el usuario acaba de escribir en los campos, con lo que ya estaba guardado.
            nuevo_titulo != art.titulo or 
            nuevo_autor != art.autor or
            nuevo_contenido != art.contenido
        )
        if hubo_cambios:
            art.titulo = nuevo_titulo
            art.autor = nuevo_autor
            art.contenido = nuevo_contenido
            st.session_state[k_guardado] = True # Guarda el estado de si hubo cambios.
        else:
            st.session_state[k_guardado] = False # No hubo cambios, se guarda como False.

    if st.session_state.get(k_guardado) is True: # Si hubo cambios, muestra un mensaje de éxito. 
        # st.session_state.get(k_guardado) recupera el estado guardado.
        # Si no hay cambios, muestra un mensaje de información.
        st.success("✅ Cambios guardados en borrador.") # Muestran mensajes de estado luego de guardar.
        # se le hace saber al usuario que ocurrió (o no) un cambio.
    elif st.session_state.get(k_guardado) is False: # el usuario apretó el botón de guardar, pero no cambió nada del artículo.
        st.info("ℹ️ No hubo cambios por guardar.") # Muestra un mensaje de información si no hubo cambios.