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
import csv

midato = []
mifichero = open('data/movimientos.csv', 'r')
lectura = csv.reader(mifichero, delimiter=',',quotechar='"')
for items in lectura:
    #print(items[0])
    midato.append(items)

print('Mi lista: ', midato[0][1])