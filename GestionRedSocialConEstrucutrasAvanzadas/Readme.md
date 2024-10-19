# Práctica II - Curso 2021/22: La Red Social CARALIBRO™

## Introducción
En esta segunda práctica, el objetivo es optimizar la aplicación desarrollada en la primera práctica
para que pueda manejar situaciones reales con hasta 1.000.000.000 de usuarios. La optimización se centrará
en reducir el tiempo de ejecución mediante el uso de estructuras de datos avanzadas.

## Descripción del Proyecto
La aplicación debe analizar la red social, detectar los grupos de usuarios (grumos) y proponer nuevas 
conexiones de amistad para aumentar la conectividad de la red, utilizando estructuras de datos más eficientes.

## Requisitos
- Python 3.x
- Librerías estándar de Python (no se requieren librerías externas)

## Uso
- Coloca el archivo de datos con las conexiones de amistad en la carpeta data/.
- Ejecuta el archivo main.py y sigue las instrucciones en pantalla para proporcionar el nombre del archivo 
  de datos y el porcentaje mínimo de usuarios que deben estar en el grumo más grande.

## Algoritmo
El algoritmo principal se basa en la búsqueda en profundidad (DFS) para detectar los grumos en la red. Los pasos son:

- Lectura del archivo de datos: Se lee el archivo de conexiones y se crea una lista de conexiones.
- Creación de la lista de usuarios: Se extraen los identificadores de usuarios de la lista de conexiones.
- Detección de grumos: Se utiliza DFS para detectar todos los usuarios de cada grumo.
- Propuesta de nuevas conexiones: Si el grumo más grande no cumple con el porcentaje mínimo requerido, se proponen nuevas 
  conexiones para unir los grumos más grandes.

## Optimización
Para mejorar la eficiencia, utilizamos estructuras de datos avanzadas como disjoint sets, pero también he implementado mi propia estructura de diccionario, y también el array de bits. 
