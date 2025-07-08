# clases/classUsuario.py

import re

class Usuario:
    def __init__(self, nombre: str, contra: str, rol: str):# Crea un nuevo usuario con nombre, contraseña y rol.
        self.nombre     = nombre
        self.contra     = contra
        self.rol        = rol
        self.borradores = []  # una lista vacía que guarda sus artículos si es publicador.

    def validar_usuario(self) -> bool: # Verifica si el nombre de usuario es válido.
        """Sólo letras, números, guiones bajos y espacios; hasta 50 chars."""
        return (
            isinstance(self.nombre, str) #es una forma de verificar que un valor es del tipo correcto. o sea una cadena de texto.
            and 1 <= len(self.nombre) <= 50 # Verifica que la longitud del nombre esté entre 1 y 50 caracteres.
            and len(self.nombre) <= 50
            and re.fullmatch(r"[A-Za-z0-9_.@\- ]*", self.nombre) is not None 
        )

    def validar_contrasena(self) -> bool:
      """12–40 caracteres, al menos un símbolo especial."""
      return (
            isinstance(self.contra, str)
            and 12 <= len(self.contra) <= 40
            and bool(re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>.,?/\\]", self.contra))
         )

    def agregar_borrador(self, articulo):
        """Añade un Articulo a esta cuenta de Publicador."""
        self.borradores.append(articulo) # Agrega un artículo a la lista de borradores del usuario.

    def __repr__(self): # Representación del objeto Usuario para facilitar la depuración.
        return f"<Usuario {self.nombre!r} rol={self.rol!r}>" 
        #f"<Usuario {self.nombre!r}	Imprime el nombre entre comillas.
        #rol={self.rol!r}>"	Muestra el rol entre comillas también.