import pyodbc
from env import *

try:
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};')
    print('Conexion exitosa!')
    cursor = conn.cursor()
    cursor.execute("SELECT @@version")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Conexión finalizada!")