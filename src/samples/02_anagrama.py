# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def verificar_anagrama(palabra1:str, palabra2:str):
    if palabra1.lower() == palabra2.lower():
        return False
    return sorted(list(palabra1.lower())) == sorted(list(palabra2.lower()))

print(verificar_anagrama("Japones", "Esponja"))
