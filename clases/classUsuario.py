# clases/classUsuario.py

import re

class Usuario:
    def __init__(self, nombre: str, contra: str, rol: str):
        self.nombre     = nombre
        self.contra     = contra
        self.rol        = rol
        self.borradores = []  # lista de Articulo

    def validar_usuario(self) -> bool:
        """Sólo letras, números, guiones bajos y espacios; hasta 50 chars."""
        return (
            isinstance(self.nombre, str)
            and len(self.nombre) <= 50
            and re.fullmatch(r"[A-Za-z0-9_ ]*", self.nombre) is not None
        )

    def validar_contrasena(self) -> bool:
        """12–20 chars, al menos un símbolo especial."""
        return (
            isinstance(self.contra, str)
            and 12 <= len(self.contra) <= 20
            and bool(re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>.,?/\\]", self.contra))
         )

    def agregar_borrador(self, articulo):
        """Añade un Articulo a esta cuenta de Publicador."""
        self.borradores.append(articulo)

    def __repr__(self):
        return f"<Usuario {self.nombre!r} rol={self.rol!r}>"
