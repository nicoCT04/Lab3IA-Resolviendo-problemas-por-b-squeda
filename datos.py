import csv

def cargar_grafo():
   grafo_costos = {}
   heuristica = {}
   
   # 1. Leer archivo de heurísticas (h)
   with open('heuristica.xlsx - Hoja1.csv', mode='r', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
         actividad = row['Activity'].strip()
         tiempo_recuperacion = int(row['Recovery time after burning 300cal (minutes)'])
         heuristica[actividad] = tiempo_recuperacion
         
   # 2. Leer archivo de conexiones y costos (g)
   with open('funcion_de_costo.xlsx - Hoja1.csv', mode='r', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
         origen = row['Origen'].strip()
         destino = row['Destino'].strip()
         costo = int(row['Cost'])
         
         if origen not in grafo_costos:
               grafo_costos[origen] = []
               
         grafo_costos[origen].append({'destino': destino, 'costo': costo})
         
   return grafo_costos, heuristica

# Probando que todo funciona:
grafo, heuristica = cargar_grafo()
print("Heurística de 'Warm-up activities':", heuristica.get('Warm-up activities'))
print("Conexiones de 'Warm-up activities':", grafo.get('Warm-up activities'))