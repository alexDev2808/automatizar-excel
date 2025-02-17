# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

import re

def eliminar_signos_puntuacion(texto):
    new_text = ""
    for letter in texto:
        if letter in r"[,;.:\"\'\[\(\]\)¡!¿?-]":
            continue
        new_text += letter
    return new_text
    
texto = """
Este es un [texto de prueba]. Este "texto" contiene varias lineas o (multilinea),
para poner a prueba la función: eliminar_signos_puntuacion; asimismo
para contar ¿Cuantas palabras existen aqui?.
Eso es todo...
¡Saludos! Equipo-TI
"""    
print(eliminar_signos_puntuacion(texto))