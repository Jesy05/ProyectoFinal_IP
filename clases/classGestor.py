# en la de clases classGestor.py

# classGestor.py

class GestorPermiso:
    CLAVES_VALIDAS = ["ClaveGestor123$", "G3st0rP@ss!", "AdminUAM_2024"]

    def __init__(self, clave_gestor):
        self.clave = clave_gestor

    def validar_pass(self):
        return (
            isinstance(self.clave, str) and
            12 <= len(self.clave) <= 20 and
            any(c in "!@#$%^&*()" for c in self.clave) and
            self.clave in GestorPermiso.CLAVES_VALIDAS
        )

