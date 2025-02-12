from conn_sqlserver import t_areas,t_Det_Funcion

areas = []
puestos = []


def asignar_valores(table, *name_col):
    new_table = []
    for row in table:
        new_table.append(dict(id_area=row[0], nombre_funcion=row[1]))
        

for area in t_areas:
    pass

for puesto in t_Det_Funcion:
    puestos.append(dict(id_area=puesto[0], nombre_funcion=puesto[1]))
    
