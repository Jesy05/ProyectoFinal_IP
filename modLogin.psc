Algoritmo  modLogin
    Definir opcion, usuario Como Cadena
    Escribir "Seleccione su rol:"
    Escribir "1. Publicador"
    Escribir "2. Lector"
    Leer opcion
	
    Si opcion = "1" Entonces
        usuario <- "Publicador"
        Escribir "Sesión iniciada como Publicador"
    Sino
        Si opcion = "2" Entonces
            usuario <- "Lector"
            Escribir "Sesión iniciada como Lector"
        Sino
            Escribir "Opción inválida"
        FinSi
    FinSi
	FinAlgoritmo
