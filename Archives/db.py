import sys 
import MySQLdb
import csv


try:
    db = MySQLdb.connect('localhost', 'root','', 'python_db')
except MySQLdb.Error as e:
    print("Error a conectar a la base de datos:", e)
    sys.exit(1)
    
try:
    cursor = db.cursor()
    cursor.execute("SELECT DISTINTC provincia FROM localidades")
    provincias = cursor.fetchall()
    for provincia in provincias:
        cursor.execute("SELECT * From localidades WHERE provincia = %s", (provincia[0],) )
        localidades = cursor.fetchall()
    with open(f'localidades_{provincia}.csv', mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["provincia", "id", "localidad", "cp", "id_prov_mstr"])
        writer.writerow(localidades)
            
except MySQLdb.Error as e:
        print("Error:", e)


db.close()

    