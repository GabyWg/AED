import functions as func

NAME_TEXT = 'envios25.txt'
#NAME_TEXT = 'envios100HC.txt'
#NAME_TEXT = 'envios100SC.txt'

letras_tup = ('B', 'C', 'K', 'H', 'U', 'X', 'W', 'E', 'P', 'Y', 'L', 'F', 'M', 'N', 'Q', 'R', 'A', 'J', 'D', 'Z', 'S', 'G', 'V', 'T')

provincias_tup = ('Provincia de Buenos Aires', 'Ciudad Autónoma de Buenos Aires', 'Catamarca', 'Chaco',
                  'Chubut', 'Córdoba', 'Corrientes','Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa','La Rioja', 
                  'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz',
                  'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán')



def principal ():
    control_r1 = None #RTA_1
    invalid_shipment = valid_shipment = 0 #RTA_2

    arch_text = func.main_arch(NAME_TEXT)

    text_line = func.read_line(arch_text)

    while text_line != '' :
        if control_r1 == None:
            control_r1 = func.type_control(text_line)
        else:
            address_flg = func.analyze_line(text_line,control_r1)
            if address_flg:
                valid_shipment += 1
            else:
                invalid_shipment += 1    
        text_line = func.read_line(arch_text)

    print(valid_shipment,"-",invalid_shipment)
    #func.print_result(control_r1, 
    #                  valid_shipment+invalid_shipment if 'Soft Control' == control_r1 else valid_shipment,
    #                  0                               if 'Soft Control' == control_r1 else invalid_shipment )
    #
    #
    #

if '__name__' == '__name__': 
    principal()
    