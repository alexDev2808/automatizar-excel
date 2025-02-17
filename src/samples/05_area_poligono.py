# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def calcular_area_poligono(*args):
    if len(args) == 1:
        return f"El area del Cuadrado es: {args[0] * args[0]}"
    if args[0] > args[1]:
        return f"El area del Rectangulo es: {args[0] * args[1]}"
    
    return f"El area del Triangulo es: {args[0] * args[1] / 2}"
    
    
print(calcular_area_poligono(3))
print(calcular_area_poligono(13,6))
print(calcular_area_poligono(3,9))