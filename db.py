import sys 
import MySQLdb as sql

try:
    db = sql.connect('localhost', 'root','', 'python_db')
except sql.Error as e:
    print("Error a conectar a la base de datos:", e)
    sys.exit(1)
print("Conexión exitosa a la base de datos")
db.close()