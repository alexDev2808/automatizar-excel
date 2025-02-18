# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

import re

alfabeto_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '/': ' '
}

def convertir_texto_morse_viceversa(texto:str):
    resultado = ""
    if re.match(r"\w+", texto, flags=re.IGNORECASE):
        for letra in texto.upper():
            if letra in alfabeto_morse:
                resultado = resultado + alfabeto_morse[letra] + " "
    else:
        codigos = texto.split(" ")
        for codigo in codigos:
            letra = next((key for key, value in alfabeto_morse.items() if value == codigo )," ")
            resultado = resultado + letra
    
    return resultado

print(convertir_texto_morse_viceversa("Hola Mundo"))
print(convertir_texto_morse_viceversa(".... --- .-.. .- / -- ..- -. -.. --- "))