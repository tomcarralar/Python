# Tomás Carretero Alarcón  
import time 
from miDisjointSetconMiDicc import *
'''
La funcion crear_red devuevle una lista que contiene todas las relciones de amistad del fichero enviado como parametro,
@param conex 
@param i: linea a paritr de la cual ya hay una relacion de amistad. 
'''
def crear_red (conex, i):
    red = []
    while i < (len(conex)):                                        #Fuerzo a que da componente del vector solo tenga 10 caracteres.

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
La funcion salvar simplemente, se asegura de que el fichero "extra.txt" de existir se vacie y luego se rellene con las nuevas 
relaicones para alcanzar el porcentaje estipulado y si no existe crearlo. 
@param unir, es el numero de grumos que hay que unir
@param grus es la lista de grumos. 
'''
def salvar(unir, grus, firstChild): 
    extra = open('extra.txt', 'w')
    extra.write('')
    extra = open('extra.txt', 'a')
    for i in range(1,unir): 
        extra.write(str(firstChild.get(grus[i-1][0])) + " " + str(firstChild.get(grus[i][0])) + "\n")
    extra.close()


name = input("Introduzca el nombre del fichero de conexiones")

inic = time.time()
fichero = open(name)                                            
conex = fichero.readlines()                                  #conex := array, del cual cada componente es una relacion en el fichero.
fichero.close()

n = (conex[0])[0:len(conex[0]) -1]                           # n := numero de usuarios de la red. 

m = (conex[1])[0:len(conex[1]) -1]                           # m := numero de realiones que contiene el fichero. 

red = crear_red(conex, 2)                                    # red := lista de tuplas que contiene las relaciones entre usuarios
t_1 = str(time.time() - inic)  
name1 = input("Introduzca el nombre del fichero de conexiones extra")
if name1 != "":                                               
    fichero = open(name1)
    conex = fichero.readlines()
    fichero.close()
    
    red = red + crear_red(conex, 0)                          # Si existe un fichero extra, a red hay que añadir las relaciones que contega. 

                               
percentage = float(input("Que porcentaje se quiere superar "))/100

t_m = time.time()

indice = -2 

x = miDisjointSet(int(n))
for relacion in red:
    (indice) = x.mdsunion(relacion[0], relacion[1], indice)

#Obtención de la lista ordenada de los grumos, en mi caso es una lista de tuplas: primer elemento id del grumo y segundo nº de usuarios
listaOrd = []
n_segura = 0
for i in range(1, int(n)+2):
    if (x.gr.get(i) != None): 
        n_segura = n_segura + x.gr.get(i)
        listaOrd.append((i, x.gr.get(i)))
t_2 = str( time.time() - t_m)
t_m = time.time()
listaOrd.sort(key=lambda x:x[1], reverse=True)      # Ordeno la lista en funcion del numero de usuarios y de mayor a menor. 

suma = 0
unir = 0
while suma/n_segura < percentage: 
    suma = suma + listaOrd[unir][1]
    unir = unir + 1
    
salvar(unir, listaOrd, x.firstChild)

t_3 = str( time.time() - t_m)
print("ANÁLISIS DE CARABIBRO\n---------------------\nFichero principal: "+ name)
print("Lectura del fichero: " + t_1 + "seg.")
print("Fichero de nuevas conexiones (pulse enter sino existe): " + name1)
print(n + " usuarios, " + m + " conexiones")
print("Porcentaje tamaño mayor grumo : " + str(percentage))
print("Creación de la estrucutra de usuarios: " + t_2 + " seg.")
print("Ordenación y selección de grumos: " + t_3 + " seg.")
print("Existen " + str(len(listaOrd)) + " grumos. ")
if unir >= 2: 
    print("Se deben unir los " + str(unir) + " grumos mayores:")
    
    for i in range(1,(unir+1)):
        print("#" + str(i-1) + ": " + str(listaOrd[i-1][1]) + " representa el (" + str(listaOrd[i-1][1]/int(n_segura)*100) + "%)")
    print("Nuevas relaicones de amistad salvadas en extra.txt")
    for i in range(0,unir - 1):
        print(str(x.firstChild.get(listaOrd[i][0])) + " <-> " + str(x.firstChild.get(listaOrd[i+1][0])))

else: 
    print("Perfecto no hacen falta conexiones")
    print("El mayor grumo contiene " + str(listaOrd[0][1]) + " usuarios que representa el (" + str(listaOrd[0][1]/int(n_segura)*100) + "%)")
