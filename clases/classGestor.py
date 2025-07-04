# en la de clases classGestor.py

# classGestor.py

class GestorPermiso: #Se define una clase llamada GestorPermiso. 
    # Sirve para manejar y validar contraseñas de gestores.

    CLAVES_VALIDAS = ["ClaveGestor123$", "G3st0rP@ss!", "AdminUAM_2024"] # Este es un atributo de clase: una lista 
    # de contraseñas que son válidas para el rol de gestor.
    # Todas las instancias (objetos) de GestorPermiso usarán esta misma lista.

    def __init__(self, clave_gestor):
        self.clave = clave_gestor # Recibe una contraseña como parámetro (clave_gestor)
        # La guarda en un atributo de instancia llamado self.clave

    def validar_pass(self): # Este método sirve para validar si la contraseña del gestor es aceptable.


        return (
            isinstance(self.clave, str) and # Primero verifica que la clave sea una cadena de texto (str).

            12 <= len(self.clave) <= 20 and # Después, se asegura de que la longitud de la clave sea entre 12 y 20 caracteres.
            any(c in "!@#$%^&*()" for c in self.clave) and # Luego, comprueba que la clave contenga al menos un 
            # símbolo especial de la lista "!@#$%^&*()".
            self.clave in GestorPermiso.CLAVES_VALIDAS #Finalmente, verifica que la clave esté dentro de la 
            # lista de CLAVES_VALIDAS.
        )

