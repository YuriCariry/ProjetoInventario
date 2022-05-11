from AplicativoInventario.models import Inventario
import csv

def run():
    f = open('C:\workspace\myenv\ProjetoInventario\scripts\inventario2022 _copia.csv', encoding='UTF8')
    csv_reader = csv.reader(f)
    for line in csv_reader:
        inventario = Inventario(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13])
        inventario.save()