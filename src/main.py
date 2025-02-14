from conn_sqlserver import t_areas,t_Det_Funcion, t_dig_area_auto,t_dig_areat,t_dig_tc, t_dig_tipoPuesto

### Formatear Datos en DB
def formatear_tabla(table, **cols):
    new_table = []
    for row in table:
        pre_row = dict()
        for key, value in cols.items():
            pre_row[key] = row[value]

        new_table.append(pre_row)
    return new_table    
    
areas = formatear_tabla(t_areas, id_area=0, nombre_area=1)
puestos = formatear_tabla(t_Det_Funcion, id_puesto=0, nombre_puesto=1)
responsables_area = formatear_tabla(t_dig_area_auto, id_res_area=0, area=1, nombre_res_area=2)
areas_internas = formatear_tabla(t_dig_areat, id_areat=0, nombre_areat=1)
tipo_puesto = formatear_tabla(t_dig_tipoPuesto, id_tipoPuesto=0, nombre_tipoPuesto=1)
nivel_puesto = formatear_tabla(t_dig_tc, id_nivelPuesto=0, nombre_nivelPuesto=1)


for res in responsables_area:
    res["colaboradores"] = []

def agregar_colaborador(responsable, colaborador):
    for res in responsables_area:
        if res["nombre_res_area"] == responsable:
            res["colaboradores"].append(colaborador)


agregar_colaborador("CARLOS GOMEZ HERNANDEZ", "PRACTICANTE DE MEJORA CONTINUA")


for res in responsables_area:
    print(res)