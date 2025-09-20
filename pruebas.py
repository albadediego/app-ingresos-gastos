#Lectura de archivos csv

'''
with open('data/movimientos.csv', 'r') as resultado:
    leer = resultado.read()
    print(type(leer))
'''
'''
resultado = open('data/movimientos.csv', 'r')
lectura = resultado.readlines()
print(type(lectura))
'''
'''
import csv

midato = []
mifichero = open('data/movimientos.csv', 'r')
lectura = csv.reader(mifichero, delimiter=',',quotechar='"')
for items in lectura:
    #print(items[0])
    midato.append(items)

print('Mi lista: ', midato[0][1])
'''
'''
#Ejemplo de regitro de datos en csv
import csv

mifichero = open('data/movimientos.csv', 'a',newline="")
lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
lectura.writerow(['16/09/2025','almuerzo','-25'])

mifichero.close()
'''
'''
from datetime import date
hoy = str(date.today())

if hoy == '2025-09-16':
    print("es hoy")
'''

#Como conseguir el ultimo id de esta lista
lista = [['1', '2025-09-01', 'Salario', '1500'], ['2', '2025-09-05', 'Ropa', '-150'], ['3', '2025-09-10', 'Supermercado', '-200']]
print(lista[-1][0])