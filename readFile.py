import csv

#Lectura del archivo
with open('localidades.csv', mode='r') as file:
     reader = csv.DictReader(file)
     for row in reader:
          print(row['localidad'], "DE",  row['provincia'].upper())
