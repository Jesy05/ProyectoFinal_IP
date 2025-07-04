Algoritmo  modGestor
    Definir opcion Como Entero
	
    Escribir "--- Módulo Gestor ---"
    Escribir "1. Listar artículos"
    Escribir "2. Aprobar artículo"
    Escribir "3. Rechazar artículo"
    Escribir "4. Publicar artículo"
    Leer opcion
	
    Segun opcion Hacer
        1:
            Escribir "Listando artículos..."
        2:
            Escribir "Artículo aprobado."
        3:
            Escribir "Artículo rechazado."
        4:
            Escribir "Artículo publicado."
        De Otro Modo:
            Escribir "Opción no válida."
    FinSegun
FinAlgoritmo
