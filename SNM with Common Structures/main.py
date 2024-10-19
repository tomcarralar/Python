# Tomás Carretero Alarcón   DNI: 04640646M 
import time  
'''
La funcion crear_red devuevle una lista que contiene todas las relciones de amistad del fichero enviado como parametro,
@param conex 
@param i: linea a paritr de la cual ya hay una relacion de amistad. 
'''
def crear_red (conex, i):
    red = []
    while i < (len(conex)):                                        #Fuerzo a que da componente del vecotr solo tenga 10 caracteres.

        nval = 1; tupla1 = ""; tupla2 = ""

        for j in range(len(conex[i])):
            num = conex[i][j]                                      # num coge del fichero el caracter i-esimo de la linea isima.
            if num == " " or num == "\n":                          # num == " " --> pasar a la segunda componente de la tupla.
                if nval == 1:                                      # num == "\n" --> ultimo caracter de la linea no debe incluirse en ninguna tupla. 
                    nval = nval + 1 

            elif nval == 1:                                        # nval == 1 implica que el caracter pertener a la pimera componente de la tupla.
                tupla1 = tupla1 + num

            else:                                                  # nval == 2 segundo componente de la tupla.
                tupla2 = tupla2 + num

        tupla = (int(tupla1), int(tupla2))
        red.append(tupla)                                          # incluyo cada relación en la lista de tuplas. 

        i +=1
    return red

'''
La funcion crear_usr devuelve la lista que contiene todos los usuarios del fichero, cada usuario con su identificador correspondiente.  
@param n: numero de usuarios totales
@param m: numero de relaiones qu hay en el fichero.  
@param red: lista de realciones entre usuarios. 
'''
def crear_usr(n, m, red): 
    usr = []
    i = 0
    while i < int(m):                                       # recorro todas las relaciones, que son tuplas por lo que comprubo que sus elementos no esten en la usr antes de volver a añadirlos. 
        if (red[i])[0] not in usr: usr.append((red[i])[0])
        if (red[i])[1] not in usr: usr.append((red[i])[1])
        i = i + 1

    return usr

'''
La funcion uber_amigos crea una lista (grumo) con todos los usuarios que están relacionados entre si. 
@param actual, es el usuario del cual se buscan todos los amigos
@param red2, es la lista de usuarios. 
@param grus, es el grumo que se está creando. 
@param asig2, es la lista de usuarios que ya han sido introuducidos o bien en este grumo u en otro. 
'''    
def uber_amigos(actual, red2, grus, asig2): 
    asig2.append(actual)                                            # introduzco el usuario actual en la lista asig
    grus.append(actual)                                             # introduzco el usuario acutal en el grumo que se está creando. 
    for j in red2:                                                  # recorro la relaciones para buscar todos los usuarios relaiconados con actual. 

        if (actual in j):                                           # Las relaciones son bidiracionales, por ello, si un elemento de la tupla es actual, 
            if int(j[1]) not in asig2:                              # el otro elemento en caso de no haber sido previamente metido al grumo se introudce, 
                grus, asig2 = uber_amigos(j[1], red2, grus, asig2)  # así como tamnién de manera recursiva se busca el resto de usuarios relaionados con el. 
                
            elif int(j[0]) not in asig2: 
                
                grus, asig2 = uber_amigos(j[0], red2, grus, asig2)

    return grus, asig2

'''
La funion ordgrus, devuelve la lista de grumos ordenada de mayor a menor en función del numero de grumos que contiene cada grumo, 
pero además también calcula el nuermo de grumos a unir para que el porcentaje de conexion sea mayor al estipulado por el usuario. 
Para la ordenación he decidido utilizar la ordenaicón por selección en lugar de utilizar ord() porque de esta manera, puedo al mismo
tiempo que ordeno los grumos, obtener el numero de estos que hay que unir para obtener el porcentaje pedido.  
@param unir, se devuelve como parametro y nos indica el numero de grumos a unir. 
@param d, es la lista de grumos. 
@param grus, es la lista de grumos que quedará ordena. 

'''
def ordgrus(unir, d, abc):
    suma = 0
    grus = []
    while len(grus) != abc:                     
        mayor = 0
        for j in range(len(d)): 
            if len(d[j]) > len(d[mayor]): 
                mayor = j
    
        grus.append(d[mayor])

        if suma/int(n) < percentage: 
            suma = suma + len(d[mayor])
            unir += 1

        d.remove(d[mayor])

    return (unir, grus)

'''
La funcion salvar simplemente, se asegura de que el fichero "extra.txt" de existir se vacie y luego se rellene con las nuevas 
relaicones para alcanzar el porcentaje estipulado y si no existe crearlo. 
@param unir, es el numero de grumos que hay que unir
@param grus es la lista de grumos. 
'''
def salvar(unir, grus): 
    extra = open('extra.txt', 'w')
    extra.write('')
    extra = open('extra.txt', 'a')
    for i in range(1,unir): 
        extra.write(str(grus[i-1][0]) + " " + str(grus[i][1]) + "\n")
    extra.close()



name = input("Introduzca el nombre del fichero de conexiones")

inic = time.time()
fichero = open(name)                                            
conex = fichero.readlines()                                  #conex := array, del cual cada componente es una relacion en el fichero.
fichero.close()

n = (conex[0])[0:len(conex[0]) -1]                           # n := numero de usuarios de la red. 

m = (conex[1])[0:len(conex[1]) -1]                           # m := numero de realiones que contiene el fichero. 

red = crear_red(conex, 2)                                    # red := lista de tuplas que contiene las relaciones entre usuarios

name1 = input("Introduzca el nombre del fichero de conexiones extra")
if name1 != "":                                               
    fichero = open(name1)
    conex = fichero.readlines()
    fichero.close()
    
    red = red + crear_red(conex, 0)                          # Si existe un fichero extra, a red hay que añadir las relaciones que contega. 

t_1 = str(time.time() - inic)                                
percentage = float(input("Que porcentaje se quiere superar "))/100



inicx = time.time()
grus = []
usr = crear_usr(n, m, red)                                  
t_2 = str( time.time() - inicx)



inicx = time.time()
abc = 0
asig = []
while abc < len(usr):                                         # Cuando un usuario no esté en la lista asig entonces se crea un grumo nuevo, caso contrario pasa al siguiente. 

    if usr[abc] not in asig: 

        grusa, asig =  uber_amigos(usr[abc], red, [], asig)   # Llamada a uber_amigos para conocer todos los miembros de un grumo. 
        grus.append(grusa)                                    # grus := es una lista de grumos, cada grumo contiene todos sus miembros. 
    
    abc += 1                                                  # Como se recorre toda la lista de usuarios, cuando un usuario está en asig aunque 
    
t_3 = str(time.time() - inicx)                                



inicx = time.time()
unir = 0
(unir, grus) = ordgrus(unir, grus, len(grus))                 # ordgrus devuelve tanto el numero de grumos a unir como la lista de grumos ordenada. 
t_4 = str(time.time() - inicx)



salvar(unir, grus)



print("ANÁLISIS DE CARABIBRO\n---------------------\nFichero principal: "+ name)
print("Lectura del fichero: " + t_1 + "seg.")
print("Fichero de nuevas conexiones (pulse enter sino existe): " + name1)
print(n + " usuarios, " + m + " conexiones")
print("Porcentaje tamaño mayor grumo : " + str(percentage))
print("Creación lista de usuarios: " + t_2 + " seg.")
print("Creación lista de grumos: " + t_3 + " seg.")
print("Ordenación y selección de grumos: " + t_4 + " seg.")
print("Existen " + str(len(grus)) + " grumos. ")
if unir >= 2: 
    print("Se deben unir los " + str(unir) + " grumos mayores:")
    
    for i in range(1,(unir+1)):
        print("#" + str(i-1) + ": " + str(len(grus[i-1])) + " representa el (" + str(len(grus[i-1])/int(n)*100) + "%)")
    print("Nuevas relaicones de amistad salvadas en extra.txt")
    for i in range(1,unir):
        print(str(grus[i-1][0]) + " <-> " + str(grus[i][1]))

else: 
    print("Perfecto no hacen falta conexiones")
    print("El mayor grumo contiene " + str(len(grus[0])) + " usuarios que representa el (" + str(len(grus[0])/int(n)*100) + "%)")