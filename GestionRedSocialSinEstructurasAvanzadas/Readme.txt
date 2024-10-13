Práctica I - Curso 2021/22: La Red Social CARALIBRO™

Introducción
Esta práctica consiste en desarrollar una aplicación para la red social ficticia CARALIBRO™, 
que se especializa en la divulgación de memes virales. La red está organizada en base a conexiones 
de amistad entre usuarios, y el objetivo es maximizar la conectividad de la red para asegurar que
los memes graciosos se distribuyan eficientemente.

Descripción del Proyecto
La aplicación debe analizar la red social, detectar los grupos de usuarios (grumos) y, si es 
necesario, proponer nuevas conexiones de amistad para aumentar la conectividad de la red.

Requisitos
Python 3.x
Librerías estándar de Python (no se requieren librerías externas)

Requisitos
Python 3.x
Librerías estándar de Python (no se requieren librerías externas)

Algoritmo
El algoritmo principal se basa en la búsqueda en profundidad (DFS) para detectar los grumos en la red. Los pasos son:
- Lectura del archivo de datos: Se lee el archivo de conexiones y se crea una lista de conexiones.
- Creación de la lista de usuarios: Se extraen los identificadores de usuarios de la lista de conexiones.
- Detección de grumos: Se utiliza DFS para detectar todos los usuarios de cada grumo.
- Propuesta de nuevas conexiones: Si el grumo más grande no cumple con el porcentaje mínimo requerido, se
  proponen nuevas conexiones para unir los grumos más grandes.

Salida
La aplicación genera un archivo extra.txt con las nuevas conexiones de amistad propuestas, si es necesario.
