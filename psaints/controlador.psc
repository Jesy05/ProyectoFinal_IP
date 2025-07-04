Algoritmo controlador
    Definir rol Como Cadena
    Definir rolNormal Como Cadena
    Definir continuar Como Caracter
	
    Repetir
        Escribir "--- Controlador Principal ---"
        Escribir "Seleccione rol: Publicador / Lector / Gestor"
        Leer rol
		
        
        rolNormal = Mayusculas(rol)
		
        Si rolNormal = "PUBLICADOR" Entonces
            Escribir "Iniciando módulo Login..."
            Escribir "Iniciando módulo Articulo..."
        Sino
            Si rolNormal = "LECTOR" Entonces
                Escribir "Iniciando módulo Login..."
                Escribir "Iniciando módulo Lector..."
            Sino
                Si rolNormal = "GESTOR" Entonces
                    Escribir "Iniciando módulo Gestor..."
                Sino
                    Escribir "Rol no válido."
                FinSi
            FinSi
        FinSi
		
        Escribir "¿Desea continuar? (S/N)"
        Leer continuar
    Hasta Que continuar = "N" o continuar = "n"
FinAlgoritmo


		
