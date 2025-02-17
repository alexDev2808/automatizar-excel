# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

def invertir_cadena_python(cadena:str):
    return cadena[::-1]
    
def invertir_cadena_manual(cadena:str):
    letters = ""
    for i in range(len(cadena) - 1,-1,-1):
        letters += cadena[i]
    return letters

print(invertir_cadena_python("Hola mundo"))
print(invertir_cadena_manual("Hola mundo"))

