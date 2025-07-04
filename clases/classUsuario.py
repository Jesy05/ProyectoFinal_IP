# classUsuario.py

import re

class Usuario:
    def __init__(self, nombre: str, contra: str):
        self.nombre = nombre
        self.contra = contra

    def validar_usuario(self):
        return (
            isinstance(self.nombre, str) and
            len(self.nombre) <= 50 and
            re.fullmatch(r"[A-Za-z0-9_ ]*", self.nombre) is not None
        )

    def validar_contrasena(self):
        return (
            isinstance(self.contra, str) and
            12 <= len(self.contra) <= 20 and
            re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>.,?/\\]", self.contra) is not None
        )
