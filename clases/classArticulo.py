# classArticulo.py

class Articulo: ## se está declarando una clase llamada Articulo.
    def __init__(self, titulo, autor, contenido, imagen=None): #Este es el método __init__, 
        # también llamado constructor.Se ejecuta automáticamente cuando se crea un 
        # nuevo objeto de la clase Articulo.
        self.titulo = titulo # # self hace referencia al objeto mismo
        # # crea un atributo llamado titulo y le asigna el valor que llegó como parámetro.
        self.autor = autor
        self.contenido = contenido
        self.imagen = imagen # Esto puede ser un objeto de tipo st.uploaded_file o una URL para que puedan decorar.

# son parámetros que se reciben al momento de crear el objeto.
