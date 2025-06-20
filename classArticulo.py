'''
Autores: Marian Alejandra Guillén Castillo
         Nora Maria Obregón Membreño
         Jesy Nicole González Jarquín

Fecha: 

Versión: (Versionado por github)

Descripción: Define la clase Articulo para gestionar publicaciones académicas.
'''

class Articulo: #Esta clase va a ser la que ayude a gestionar 
    #las acciones relacionadas con los artículos académicos.
    def __init__(self, titulo, autor, contenido): # estos son los parametros que va a majenar
        
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        self.estado = "Pendiente" #esto no es un parametro, es un atributo que se le asigna al objeto
        self.revisiones = 0 #esto es un contador de revisiones, empieza en 0 para que el que revisa sepa 
        #que no ha sido revisado o cuantas veces ha sido revisado

    def aprobar(self): 
        self.revisiones += 1
        if self.revisiones >= 2:
            self.estado = "Aprobado"

    def rechazar(self):
        self.estado = "Rechazado"

    def mostrar(self):
        print("=" * 50)
        print(f"📘  TÍTULO: {self.titulo}")
        print(f"✍️  AUTOR: {self.autor}")
        print(f"📄  CONTENIDO:\n{self.contenido}")
        print(f"✅  ESTADO: {self.estado}")
        print("=" * 50 + "\n") #la operacion hace que se imprima una linea de 50 caracteres