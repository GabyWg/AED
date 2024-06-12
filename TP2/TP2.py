__Author__ = 'TP1-G457'
prueba = 1

############ Datos de ISO 3166-2:AR ############

letras_tup = ('B', 'C', 'K', 'H', 'U', 'X', 'W', 'E', 'P', 'Y', 'L', 'F', 'M', 'N', 'Q', 'R', 'A', 'J', 'D', 'Z', 'S', 'G', 'V', 'T')

provincias_tup = ('Provincia de Buenos Aires', 'Ciudad Autónoma de Buenos Aires', 'Catamarca', 'Chaco',
                  'Chubut', 'Córdoba', 'Corrientes','Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa','La Rioja', 
                  'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz',
                  'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán')
#sdffsdfsdsdf
############ Ingreso de datos ############

# cp =  input('Ingrese el código postal del lugar de destino: ')
# direccion = input('Dirección del lugar de destino: ')
# tipo = int(input('Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): '))
# pago = int(input('Forma de pago (1: efectivo - 2: tarjeta): '))

############ Eleccion del destino y aumento del envio ############

if cp.isdigit():
    if len(cp) == 4:
        destino = 'Bolivia'
        aumento_inter = 1.20
    elif len(cp) == 5:
        destino = 'Uruguay'
        aumento_inter = 1.2 if cp[0] == '1'  else 1.25
    elif len(cp) == 6:
        destino = 'Paraguay'
        aumento_inter = 1.20
    elif len(cp) == 7:
        destino = 'Chile'
        aumento_inter = 1.25
    else:
        destino = 'Otro'
        aumento_inter = 1.5
else:
    if len(cp) == 8:
        if cp[0].isalpha() and cp[-1].isalpha() and cp[-2].isalpha() and cp[-3].isalpha():
            if not(cp[0].upper() == 'I' or cp[0].upper() == 'O' ):
                destino = 'Argentina'
                aumento_inter = 1
            else:
                destino = 'Otro'
                aumento_inter = 1.5
        else:
            destino = 'Otro'
            aumento_inter = 1.5
    elif len(cp) == 9 and cp[5] == '-' and cp.replace('-', '').isdigit():
        destino = 'Brasil'
        if cp[0] == '8' or cp[0] == '9':
            aumento_inter = 1.20
        elif cp[0] == '0'  or cp[0] == '1'  or cp[0] == '2'  or cp[0] == '3':
            aumento_inter = 1.25
        else:
            aumento_inter = 1.30
    else:
        destino = 'Otro'
        aumento_inter = 1.5

############ Eleccion de la pronvincia ############

if destino != 'Argentina':
    provincia = 'No Aplica'
else:
    provincia = provincias_tup[letras_tup.index(cp[0])] # Revisar si se puede usar esto y sino if elif infinito

############ Precio del envio ############

if  tipo == 0:
    precio = 1100 
elif tipo == 1:
    precio = 1800 
elif tipo == 2:
    precio = 2450 
elif tipo == 3:
    precio = 8300 
elif tipo == 4:
    precio = 10900 
elif tipo == 5:
    precio = 14300
else:
    precio = 17900

############ Precio inicial del envio con el aumento segun destino ############

inicial = int(precio * aumento_inter)

############ Precio Final del envio con el formato de pago ############

final = int( inicial * (0.9 if pago == 1 else 1) )

############ Impresion de resultados  ############


# print(' (r1) - Tipo de control de direcciones:', control)
# print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
# print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
# print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
# print(' (r5) - Cantidad de cartas simples:', ccs)
# print(' (r6) - Cantidad de cartas certificadas:', ccc)
# print(' (r7) - Cantidad de cartas expresas:', cce)
# print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
# print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
# print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
# print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
# print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
# print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
# print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)