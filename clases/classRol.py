# classRol.py

class Rol: #Se define una clase llamada Rol. Es una plantilla para crear objetos que representen roles de usuarios.

    ROLES_VALIDOS = ["Publicador", "Gestor", "Lector"] #Aquí se define un atributo de clase, es decir, 
    # una variable que no cambia entre objetos. Todos los objetos de la clase Rol comparten esta misma lista.
    #ROLES_VALIDOS contiene los únicos nombres de rol que se consideran válidos.

    def __init__(self, rol): #Este es el constructor, y se ejecuta cuando se crea un nuevo objeto Rol.
        self.rol = rol # recibe un parámetro rol (por ejemplo: "Gestor").
        # Guarda ese valor en self.rol, que es un atributo de instancia (individual para cada objeto).

    def validar_rol(self):
        return self.rol in Rol.ROLES_VALIDOS  # sirve para verificar si el rol ingresado es válido.
# Usa self.rol, que es el valor del rol que tiene el objeto.
# Lo busca dentro de Rol.ROLES_VALIDOS.
# Devuelve True si está en la lista, o False si no lo está.

usuarios_guardados = {
    "ana_publicadora": {"contra": "Ana*12345678", "rol": "Publicador"},
    "luis_lector": {"contra": "Luis*12345678", "rol": "Lector"}
}