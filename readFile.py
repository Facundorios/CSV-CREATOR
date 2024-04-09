import csv

#Lectura del archivo
# with open('localidades.csv', mode='r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['localidad'], "DE",  row['provincia'].upper())
        
        
data = [['Localidad', 'Provincia',],
        ['Buenos Aires', 'Buenos Aires'],
        ['Cordoba', 'Cordoba'],
        ['Rosario', 'Santa Fé']
        ]

with open('localidades_nuevas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)