import random
#Adivina el numero computadora


def adivina_el_numero_computadora(x):
    print("=========================")
    print("  ¡Bienvenido al Juego!")
    print("=========================")
    print(f"Piensa un número entre 1 y {x} para que la computadora intente adivinarlo...")
    
    limite_inferior = 1 
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        # Generar una predicción
        if limite_inferior != limite_superior: #[1, 10]
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #también podría ser el limite superior
            
        #Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower() #lo que ingrese en input, lo convierte a letras minúsculas
        
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Siii! La computadora adivinó tu número correctamente: {prediccion}")
            
            
adivina_el_numero_computadora(10)  
        #intervalo inicial: [1, 10]
        #Predicción: 6
        #Respuesta: "a"
        #Intervalo: [1, 5]
        
        