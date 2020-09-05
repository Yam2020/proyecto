#Yamile Saray García Rivera
#A01703397
#Avance 2_proyecto

#Lista de  de 7 preguntas (notas)
#Ciclo while la cantidad de preguntas sean < = 7
#If else, ara saber si la respuesta es corrcta o incorrecta
# Una variable contador, contador_respuesta_correcta

#Funcion para mostrar preguntas
#No regresa ningun valor (return)
def mostrar_pregunta (numero_pregunta):
    #aqui todo el codigo
    print ("¿Pregunta " + str(numero_pregunta) + "?")
    print ("¡Animo tu puedes!")

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
            print("Respuesta incorrecta")
            
        
    if numero_pregunta == 2:
        if respuesta == "re":
            print("Respuesta correcta")
            booRespuesta = True 
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta")
            
            
    if numero_pregunta == 3:
        if respuesta == "mi":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta")
            
    
    if numero_pregunta == 4:
        if respuesta == "fa":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta")
            
            
    if numero_pregunta == 5:
        if respuesta == "sol":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta")
            
            
    if numero_pregunta == 6:
        if respuesta == "la":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta")
      
    if numero_pregunta == 7:
        if respuesta == "si":
            print("Respuesta correcta")
            booRespuesta = True
            #contador_respuesta = contador_respuesta_correcta + 1
        
        else:
            booRespuesta = False
            print("Respuesta incorrecta")
            
    
    return (booRespuesta)
            
            
        
#Prueba 1     
print ("Bienvenido a Aprende Música Facil")
print ("***")
print ("***")
print ("")

#Declaramos variable que cuenta respuesta correctas.
contador_respuesta_correcta = 0

#Pregunta 1 
mostrar_pregunta (1)
dato_entrada_1 = input("Nombre de la nota que se encuentra en el tercer espacio del pentagrama : ")

booAlmacena = evaluar_respuesta (1, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1


#Pregunta 2
mostrar_pregunta (2)
dato_entrada_1 = input("Nombre de la nota que se encuentra en la cuarta línea del pentagrama : ") 

booAlmacena = evaluar_respuesta (2, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1



#Pregunta 3
mostrar_pregunta (3)
dato_entrada_1 = input("Nombre de la nota que se encuentra en el cuarto espacio del pentagrama : ") 

booAlmacena = evaluar_respuesta (3, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1



#Pregunta 4
mostrar_pregunta (4)
dato_entrada_1 = input("Nombre de la nota que se encuentra en el primer espacio del pentagrama : ") 

booAlmacena = evaluar_respuesta (4, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1



#Pregunta 5
mostrar_pregunta (5)
dato_entrada_1 = input("Nombre de la nota que se encuentra en la segunda línea del pentagrama : ") 

booAlmacena = evaluar_respuesta (5, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1

#Pregunta 6
mostrar_pregunta (6)
dato_entrada_1 = input("Nombre de la nota que se encuentra en el segundo espacio del pentagrama : ") 

booAlmacena = evaluar_respuesta (6, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1
    
#Pregunta 7
mostrar_pregunta (7)
dato_entrada_1 = input("Nombre de la nota que se encuentra en la tercer línea del pentagrama : ") 

booAlmacena = evaluar_respuesta (7, dato_entrada_1)

if booAlmacena == True:
    contador_respuesta_correcta = contador_respuesta_correcta + 1


#Cuando trae contador_respuesta_correcta nos dice cuantas veces lo hizo bien el usuario. 
print (" Total de respuestas correctas " + str(contador_respuesta_correcta))



    
    
    
    
    




