def jugar(intento : int =1 ):       #cuando ponemos = a algo estamos insertando valor por default
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta.lower() != "naranja":  #si la respuesta ingresada es difernte de naranja
        if intento < 3:
            print("\nFallaste! Inténtalo de nuevo")             
            intento += 1 
            jugar(intento)  # Llamada recursiva         
        else:
            print("\nPerdiste!")     
    else:
        print("\nGanaste!")

#30:00