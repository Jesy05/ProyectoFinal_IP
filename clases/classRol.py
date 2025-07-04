# classRol.py

class Rol:
    ROLES_VALIDOS = ["Publicador", "Gestor", "Lector"]

    def __init__(self, rol):
        self.rol = rol

    def validar_rol(self):
        return self.rol in Rol.ROLES_VALIDOS
