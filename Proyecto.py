#Yamile Saray García Rivera
#A01703397
#Avance_4_proyecto

#Nota Futura: Cuando me enseñen "listas" planeao agrupar mis respuestas, para simplificar el codigo.

#Hola mundo 

#Lista de 7 preguntas (notas)
#Funciones
#If else, para saber si la respuesta es correcta o incorrecta
#Ciclo while la cantidad de preguntas sean < = 7


#Funcion para mostrar preguntas
#No regresa ningun valor (return)
def mostrar_pregunta (numero_pregunta):
    #aqui todo el codigo
    if numero_pregunta == 1:
        print("¿Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en el tercer espacio del pentagrama? ")
    if numero_pregunta == 2:
        print ("Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en la cuarta línea del pentagrama? ")
    if numero_pregunta == 3:
        print("Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en el cuarto espacio del pentagrama? ")
    if numero_pregunta == 4:
        print("Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en el primer espacio del pentagrama? ")
    if numero_pregunta == 5:
        print ("Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en la segunda línea del pentagrama? ")
    if numero_pregunta == 6:
        print("Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en el segundo espacio del pentagrama? ")
    if numero_pregunta == 7:
        print("Pregunta " + str(numero_pregunta) + ": Nombre de la nota que se encuentra en la tercer línea del pentagrama? ")
        
        
#Regresa verdadero en caso de que la respuesta sea correcta
#Regresa falso, si es incorrecta
def evaluar_respuesta (numero_pregunta, respuesta):
    
    booRespuesta = False 
    
    if numero_pregunta == 1:
        if respuesta == "do":
            print("Respuesta correcta")
            booRespuesta = True 
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False  #No es necesario ya que esta inicializando en falso
            print("Respuesta incorrecta, intentalo de nuevo")
            
        
    if numero_pregunta == 2:
        if respuesta == "re":
            print("Respuesta correcta")
            booRespuesta = True 
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta, intentalo de nuevo")
            
            
    if numero_pregunta == 3:
        if respuesta == "mi":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta, intentalo de nuevo")
            
    
    if numero_pregunta == 4:
        if respuesta == "fa":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta, intentalo de nuevo")
            
            
    if numero_pregunta == 5:
        if respuesta == "sol":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta, intentalo de nuevo")
            
            
    if numero_pregunta == 6:
        if respuesta == "la":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta, intentalo de nuevo")
      
    if numero_pregunta == 7:
        if respuesta == "si":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta, intentalo de nuevo")
            
    
    return (booRespuesta)
            
            
        
#Prueba 1     
print ("Bienvenido a Aprende Música Facil")
print ("***")
print ("***")
print ("")

#Declaramos variable que cuenta las preguntas. 
numero_de_pregunta = 1

#Empezamos con un ciclo while, para que muestra las 7 preguntas.  
while numero_de_pregunta <= 7:
    
    #Se muestra al usuario la pregunta, mandando a llamar la función mostrar_pregunta.
    mostrar_pregunta(numero_de_pregunta)
    #El usuario introduce el dato (Entrada).
    dato_entrada_respuesta = input ("Intruduce la respuesta correcta: ")
    #Se manda a llamar la función evaluar_respuesta, esta variable booAlmacena guarda la evaluación.
    booAlmacena = evaluar_respuesta (numero_de_pregunta, dato_entrada_respuesta)
    
    #Ahora llamamos la variable que contiende la función evaluar_respuesta, para evaluar si es verdadera prosiga con la siguiente pregunta. 
    if booAlmacena == True:
        numero_de_pregunta = numero_de_pregunta + 1