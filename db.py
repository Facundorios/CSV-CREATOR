import sys 
import MySQLdb
import csv

try:
    db = MySQLdb.connect('localhost', 'root','', 'python_db')
except MySQLdb.Error as e:
    print("Error a conectar a la base de datos:", e)
    sys.exit(1)
print("Base de datos exitosa")

with open("localidades.csv", 'r', encoding="utf-8") as file:
    lector = csv.reader(file, delimiter=',', quotechar='"')
    header = next(lector)

create_tables = "CREATE TABLE IF NOT EXISTS localidades (provincia VARCHAR(100) NOT NULL, id INT NOT NULL, localidad VARCHAR(100) NOT NULL,cp INT(255) NOT NULL,id_prov_mstr INT(255));"

csv_content = "INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s);" % ("provincia", "id", "localidad", "cp", "id_prov_mstr")

cursor = db.cursor()
cursor.execute(create_tables)
db.commit() 
#cursor.execute(csv_content)
db.commit()

for localidad in lector:
    cursor.execute(f"INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES ({localidad[0]}, {localidad[1]}, {localidad[2]}, {localidad[3]}, {localidad[4]})")
db.commit()

try:
    cursor.execute("SELECT DISTINCT provincia from localidades")
    provincias = cursor.fetchall()
    for provincia in provincias:
        cursor.execute("SELECT * FROM `localidades` WHERE provincia = %s", (provincia[0],))
        localidades = cursor.fetchall()
        with open(f'Archives/{provincia[0]}.csv', "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(localidades)
            
except MySQLdb.Error as e:
        db.rollback()
        print("Error:", e)


db.close()

    