
from os import system
import os.path
import pickle
import csv

CSV_ARCH = 'envios-tp4.csv'
BINARY_ARCH = 'envios-tp4.dat'  


def main_arch(name_arch, mode, flg_open = True, arch = None): #Funcion que abre el archivo que se le envia, al finalizar la lectura se le enviar otros parametros de otra funcion para cerrar el mismo
    if flg_open:
        if mode[0] == 'r':
            if  os.path.exists(name_arch):
                return open(name_arch,mode)
            else:
                print("El archivo no existe!")
        else:
            return open(name_arch,mode)
    else:
        (arch.close() for arch in range(len(arch)))


arch_csv = main_arch(CSV_ARCH,'rt')

for text_line in arch_csv:
    print(text_line)