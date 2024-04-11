#Importaciones
import sys
import csv
import MySQLdb

#Conexión a la base de datos.
try:
    db = MySQLdb.connect("localhost", "root", "", "python_db")
except MySQLdb.Error as e:
    print("Error a conectar a la base de datos:", e)
    sys.exit(1)
print("Conexión a la base de datos exitosa")

#Cursor para ejecutar las consultas.
cursor = db.cursor()

# Eliminar la tabla en caso de que ya existan.
try:
    cursor.execute("DROP TABLE IF EXISTS localidades")
    db.commit()
except MySQLdb.Error as e:
    db.rollback()
    print("Error al eliminar la tabla:", e)


#Creación de la tabla y sus filas.
try:
    create_tables = "CREATE TABLE IF NOT EXISTS localidades (provincia VARCHAR(100) NOT NULL, id INT NOT NULL, localidad VARCHAR(100) NOT NULL,cp INT(255) NOT NULL,id_prov_mstr INT(255));"
    cursor.execute(create_tables)
    db.commit()
except MySQLdb.Error as e:
    db.rollback()
    print("Error:", e)
print("Tabla creada con éxito")

#Insertar datos en la tabla.

#Forma antigua (al rededor de 20 segundos de carga.)

# try:
#     with open("localidades.csv", newline="") as archivo_csv:
#         lector_csv = csv.reader(archivo_csv, delimiter=",", quotechar='"')
#         header = next(lector_csv)
#         for provincia in lector_csv:
#             add_localities = f'INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES ("{provincia[0]}", "{provincia[1]}", "{provincia[2]}", "{provincia[3]}", "{provincia[4]}")'
#             cursor.execute(add_localities)
#             db.commit()
# except MySQLdb.Error as e:
#     db.rollback()
#     print("Error:", e)
# print("Datos insertados con éxito")


#Nuevo metodo, su principal diferencia es el metodo executemany(), un metodo que toma 2 argumentos, por lo que tambien se diferencia que que se insertan todos los datos juntos, primero definiendo "localidades" como un arreglo con todos los valores de las filas con un "for in", por otro lado un "add_localities", una variable con la primera parte de la consulta sql.


try:
    with open("localidades.csv", newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=",", quotechar='"')
        header = next(lector_csv)
        localidades = [(fila[0], fila[1], fila[2], fila[3], fila[4]) for fila in lector_csv]
        add_localities = "INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(add_localities, localidades)
        db.commit()
except MySQLdb.Error as e:
     db.rollback()
     print("Error:", e)
print("Datos insertados con éxito")



#Crear archivos CSV por provincia.
try:
    cursor.execute("SELECT DISTINCT provincia from localidades")
    provincias = cursor.fetchall()
    for provincia in provincias:
        cursor.execute(
            "SELECT * FROM `localidades` WHERE provincia = %s", (provincia[0],)
        )
        localidades = cursor.fetchall()
        with open(
            f"csv/Localidades de {provincia[0]}.csv", "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(localidades)
except MySQLdb.Error as e:
    db.rollback()
    print("Error:", e)
print("Archivos CSV creados con éxito")


db.close()
