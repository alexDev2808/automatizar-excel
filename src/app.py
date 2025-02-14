import pandas as pd
from tabulate import tabulate
from main import *
from openpyxl import load_workbook


wb = load_workbook('PNuevoIngreso.xlsx')
hoja = wb.active

sin_datos = []

def generar_formato_tabla():
    datos = []
    headers = ["NoEmp","Nombre","APP","APM","Puesto","Empresa","Fecha","Correo"]
    formato_datos = []

    for fila in hoja.iter_rows(values_only=True):
        datos.append(dict(zip(headers, fila)))

    for index, usuario in enumerate(datos):
        if index == 0:
            continue
        pre_formato = dict()
        pre_formato["id_empleado"] = f"0{str(usuario["NoEmp"])}"
        pre_formato["app"] = usuario["APP"]
        pre_formato["apm"] = usuario["APM"]
        pre_formato["nombre"] = usuario["Nombre"]
        pre_formato["activo"] = 1
        pre_formato["pass"] = f"{usuario["APP"]}0{str(usuario["NoEmp"])}"
        pre_formato["mail"] = usuario["Correo"]
        pre_formato["id_area_res2"] = 5
        pre_formato["id_area_res3"] = "0"
        pre_formato["perm_fsm"] = "0"
        
        pre_formato["id_area"] = buscar_en_tabla(areas, "area", usuario["Empresa"])
        pre_formato["id_funcion"] = buscar_en_tabla(puestos, "puesto", usuario["Puesto"])
        
        
        formato_datos.append(pre_formato)

    return formato_datos


def buscar_en_tabla(tabla, nombre_columna, valor_buscar):
    for item in tabla:
        if valor_buscar == item[f"nombre_{nombre_columna}"]:
            return item[f"id_{nombre_columna}"]
    sin_datos.append(dict( columna = f"id_{nombre_columna}", valor_buscado = valor_buscar ))
    return None


def generar_tabla_excel(datos):
    id_empleado = []
    app = []
    apm = []
    
    for fila in datos:
        id_empleado.append(fila["id_empleado"])
        app.append(fila["app"])
        apm.append(fila["apm"])
    

    exportar_datos = { "id_empleado": id_empleado,"app": app,"apm": apm}

    df = pd.DataFrame(exportar_datos)
    
    df.to_excel("files/datos_sql.xlsx", index=False)
    
  
# formato_datos = generar_formato_tabla()
# if sin_datos != []:
#     print(f"Faltan datos: --- {sin_datos} ---")
    
# print("Datos correctos... Generando datos.")
# generar_tabla_excel(formato_datos)

