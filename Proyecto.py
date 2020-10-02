#Yamile Saray García Rivera
#A01703397
#Avance_5_proyecto

#Funciones
#If else, para saber si la respuesta es correcta o incorrecta
#Funciones 
#Ciclo while la cantidad de preguntas sean < = 7
#Lista de 7 preguntas (notas)


#Funciones "mostrar_pregunta" y "Evaluar respuesta"; son para nuestro primer nivel. 

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


##################################################
#Funciones para Nivel 2. Donde tendremos dos funciones "crear_pregunta" y "crear_respuestas" utilizando listas. 

#Funcion donde almacena las pregunta al usuario. Son cinco en total. 
def crear_pregunta():
    arrPreguntas = []
    arrPreguntas.append ("Pregunta 1: ¿Duración de la nota redonda? ")
    arrPreguntas.append ("Pregunta 2: ¿Duración de la nota blanca? ")
    arrPreguntas.append ("Pregunta 3: ¿Duración de la nota negra? ")
    arrPreguntas.append ("Pregunta 4: ¿Duración de la nota corchea? ")
    arrPreguntas.append ("Pregunta 5: ¿Duración de la nota Semicorchea? ")
    
    return arrPreguntas

#Función donde almacena las respuestas correctas. 
def crear_respuestas():
    arrRespuestas = []
    arrRespuestas.append ("Cuatro tiempos")
    arrRespuestas.append ("Dos tiempos")
    arrRespuestas.append ("Un tiempo")
    arrRespuestas.append ("Medio tiempo")
    arrRespuestas.append ("Un cuarto")
     
    return arrRespuestas

#Creamos Preguntas en formar de variables. 
arreglosPreguntasNivel2 = crear_pregunta ()
arreglosRespuestaNivel2 = crear_respuestas ()

#############################################
#Bievenida al usuario. 

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
        
#########################################################
#Segundo Nivel, donde llamaremos a nuestras funciones "crear_pregunta" y "crear_respuestas"

#Lo inicializamos en cero, así empieza nuestra lista. 
print ("***")
print ("***")
print ("")
print ("Segundo Nivel")
contador = 0 
limite_maximo = (len(arreglosPreguntasNivel2) - 1)  #arreglosPreguntasNivel2 su longitud es igual a 2, porque cuenta la cantidad de elementos en la lista.  

#Máximo igual a 1: en este caso tenemos nuestro límite de 2 preguntas. 
while contador <= limite_maximo:
    Pregunta = arreglosPreguntasNivel2 [contador]
    
    print (Pregunta)
    Respuesta = arreglosRespuestaNivel2 [contador]
    dato_entrada = input("Introduce la respuesta correcta: ")
    
    if dato_entrada == Respuesta:
        print ("Correcto")
        contador = contador + 1 
        
    else:
        print ("Incorrecto")
        