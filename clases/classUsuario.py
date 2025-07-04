# classUsuario.py

import re # es una librería para trabajar con expresiones regulares como validaciones de cadenas

class Usuario:
    def __init__(self, nombre: str, contra: str):
        self.nombre = nombre
        self.contra = contra

    def validar_usuario(self):
        return (
            isinstance(self.nombre, str) and
            len(self.nombre) <= 50 and
            re.fullmatch(r"[A-Za-z0-9_ ]*", self.nombre) is not None # Acepta letras, números, guiones bajos y espacios
        ) # re.fullmatch asegura que toda la cadena cumpla con el patrón

    def validar_contrasena(self):
        return (
            isinstance(self.contra, str) and
            12 <= len(self.contra) <= 20 and
            re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>.,?/\\]", self.contra) is not None
        )
