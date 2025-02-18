# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def convertir_decimal_binario(numero:int):
    if numero == 0:
        return 0
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    
    return binario    

numero = 8
resultado = convertir_decimal_binario(numero)
print(f"El binario de {numero} es: {resultado}")