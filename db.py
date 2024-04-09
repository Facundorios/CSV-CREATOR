import sys 
import MySQLdb

try:
    db = MySQLdb.connect('localhost', 'root','', 'python_db')
except MySQLdb.Error as e:
    print("Error a conectar a la base de datos:", e)
    sys.exit(1)

sql="SELECT * FROM localidades WHERE provincia = 'Formosa'" 
cursor = db.cursor()


#Primera consulta
try:
    cursor.execute(sql)
    localidades = cursor.fetchall()
    for localidad in localidades:
        print(localidad[0],localidad[1],localidad[2],localidad[3],localidad[4])
except MySQLdb.Error as e:
    print("Error:", e)
db.close()
    