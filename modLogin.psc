Algoritmo  modLogin
    Definir opcion, usuario Como Cadena
    Escribir "Seleccione su rol:"
    Escribir "1. Publicador"
    Escribir "2. Lector"
    Leer opcion
	
    Si opcion = "1" Entonces
        usuario <- "Publicador"
        Escribir "Sesi�n iniciada como Publicador"
    Sino
        Si opcion = "2" Entonces
            usuario <- "Lector"
            Escribir "Sesi�n iniciada como Lector"
        Sino
            Escribir "Opci�n inv�lida"
        FinSi
    FinSi
	FinAlgoritmo
