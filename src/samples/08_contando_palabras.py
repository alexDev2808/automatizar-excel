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
    texto_sin_saltos_linea = re.sub(r"\n", "", texto)
    return re.sub(r"[,;.:\"\'\[\(\]\)¡!¿?-]", "", texto_sin_saltos_linea)
   
def eliminar_espacios(texto:str):
    return re.sub(r"^\s+|\s+$", "", texto)
     
def contar_palabras(texto:str):
    texto_dividido = texto.lower().split(" ")
    palabras_unicas = set(texto_dividido)
    mapa_palabras = [ {"palabra": palabra, "repeticiones": 0} for palabra in palabras_unicas ]
    for palabra in texto_dividido:
        for palabra_unica in mapa_palabras:
            if palabra_unica["palabra"] == palabra:
                palabra_unica["repeticiones"] += 1
    return mapa_palabras
    
texto = """
Este es un [texto de prueba]. Este "texto" contiene varias lineas o (multilinea), 
para poner a prueba la función: eliminar_signos_puntuacion; asimismo 
para contar ¿Cuantas palabras existen aqui ?.
Eso es todo ...

¡Saludos! Equipo-TI
"""    

# texto_formateado = eliminar_signos_puntuacion(texto)
# texto_formateado = eliminar_espacios(texto_formateado)

# resultado = contar_palabras(texto_formateado)
# for palabra in resultado:
#     print(palabra)
    
text = "Pablito clavo un clavito en la calva de un calvito Pablito clavo un clavito"
    
def countWords(text:str):
    words_map = dict()
    for key in text.lower().replace(r"^a-z0-9", " ").split(" "):
        if key in words_map:
            words_map[key] += 1
        else:
            words_map[key] = 1
    return words_map   
 
print(countWords(text))