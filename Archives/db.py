import sys 
import MySQLdb
import csv

try:
    db = MySQLdb.connect('localhost', 'root','', 'python_db')
except MySQLdb.Error as e:
    print("Error a conectar a la base de datos:", e)
    sys.exit(1)
print("Base de datos exitosa")

try:
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT provincia from localidades")
    provincias = cursor.fetchall()
    for provincia in provincias:
        cursor.execute("SELECT * FROM `localidades` WHERE provincia = %s", (provincia[0],) )
        localidades = cursor.fetchall()
        with open(f'Archives/{provincia[0]}.csv', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(localidades)
            
except MySQLdb.Error as e:
        db.rollback()
        print("Error:", e)


db.close()

    