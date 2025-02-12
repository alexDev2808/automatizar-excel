import pyodbc
from env import *

try:
    print('Realizando conexión...')
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};')
    print('Conexion exitosa!')
    print('Realizando consultas!')
  
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Areas')
    t_areas = cursor.fetchall()
    
    cursor.execute('SELECT * FROM Det_Funcion')
    t_Det_Funcion = cursor.fetchall()    
    
    cursor.execute('SELECT * FROM dig_area_auto')
    t_dig_area_auto = cursor.fetchall()
    
    cursor.execute('SELECT * FROM dig_tc')
    t_dig_tc = cursor.fetchall()
    
    cursor.execute('SELECT * FROM dig_areat')
    t_dig_areat = cursor.fetchall()
    
    cursor.execute('SELECT * FROM dig_tipoPuesto')
    t_dig_tipoPuesto = cursor.fetchall()
    
    
except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Conexión finalizada!")