Algoritmo  modGestor
    Definir opcion Como Entero
	
    Escribir "--- M�dulo Gestor ---"
    Escribir "1. Listar art�culos"
    Escribir "2. Aprobar art�culo"
    Escribir "3. Rechazar art�culo"
    Escribir "4. Publicar art�culo"
    Leer opcion
	
    Segun opcion Hacer
        1:
            Escribir "Listando art�culos..."
        2:
            Escribir "Art�culo aprobado."
        3:
            Escribir "Art�culo rechazado."
        4:
            Escribir "Art�culo publicado."
        De Otro Modo:
            Escribir "Opci�n no v�lida."
    FinSegun
FinAlgoritmo
