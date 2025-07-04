# classArticulo.py

class Articulo:
    def __init__(self, titulo, autor, contenido, imagen=None): 
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        self.imagen = imagen # Esto puede ser un objeto de tipo st.uploaded_file o una URL para que puedan decorar

