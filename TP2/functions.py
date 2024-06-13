def main_arch(name_text, flg_open = True, arch = None):
    if flg_open:
        arch = open(name_text,'rt')
        return arch
    else:
        arch.close()

def read_line(arch_texto):
    text_line = arch_texto.readline()
    if  text_line == '':
        main_arch('-1', False, arch_texto)  
    return text_line

def type_control(line_text):
    return 'Hard Control' if 'HC' in line_text.upper() else 'Soft Control'

def analyze_line (text_line,control): 
    codpos_line,address_line,id_type_shipment_line,waypay_line = text_line[:9].strip(),text_line[9:29].strip(),int(text_line[29]),int(text_line[30]) 
    
    country,province,charge_shipment = analyze_codpos(codpos_line)
    
    cost_shipment = calculate_shipment(charge_shipment,id_type_shipment_line,waypay_line)
    
    address_flg = True if 'Soft Control' == control else valid_address(address_line) 
    
    return address_flg,cost_shipment,id_type_shipment_line,codpos_line

def analyze_codpos(cod_pos):

    letter_tup = ('B', 'C', 'K', 'H', 'U', 'X', 'W', 'E', 'P', 'Y', 'L', 'F', 'M', 'N', 'Q', 'R', 'A', 'J', 'D', 'Z', 'S', 'G', 'V', 'T')

    prov_tup = ('Provincia de Buenos Aires', 'Ciudad Autónoma de Buenos Aires', 'Catamarca', 'Chaco',
                    'Chubut', 'Córdoba', 'Corrientes','Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa','La Rioja', 
                    'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz',
                    'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán')
    
    cod_pos = cod_pos.upper()

    if cod_pos.isdigit():
        if len(cod_pos) == 4:
            country_codpos = 'Bolivia'
            charge_shipment_codpos = 1.20
        elif len(cod_pos) == 5:
            country_codpos = 'Uruguay'
            charge_shipment_codpos = 1.2 if cod_pos[0] == '1'  else 1.25
        elif len(cod_pos) == 6:
            country_codpos = 'Paraguay'
            charge_shipment_codpos = 1.20
        elif len(cod_pos) == 7:
            country_codpos = 'Chile'
            charge_shipment_codpos = 1.25
        else:
            country_codpos = 'Otro'
            charge_shipment_codpos = 1.5
    else:
        if len(cod_pos) == 8:
            if 'AAAA' <= (cod_pos[0] + cod_pos[5:8]) <= 'ZZZZ': #cod_pos[0].isalpha() and cod_pos[-1].isalpha() and cod_pos[-2].isalpha() and cod_pos[-3].isalpha():
                if not(cod_pos[0].upper() in ('I','O') ):
                    country_codpos = 'Argentina'
                    charge_shipment_codpos = 1
                else:
                    country_codpos = 'Otro'
                    charge_shipment_codpos = 1.5
            else:
                country_codpos = 'Otro'
                charge_shipment_codpos = 1.5
        elif len(cod_pos) == 9 and cod_pos[5] == '-' and cod_pos.replace('-', '').isdigit():
            country_codpos = 'Brasil'
            if  cod_pos[0] in ('8','9'): 
                charge_shipment_codpos = 1.20
            elif '0' <= cod_pos[0] <= '3': 
                charge_shipment_codpos = 1.25
            else:
                charge_shipment_codpos = 1.30
        else:
            country_codpos = 'Otro'
            charge_shipment_codpos = 1.5

    if country_codpos != 'Argentina':
        province_codpos = 'No Aplica'
    else:
        province_codpos = prov_tup[letter_tup.index(cod_pos[0])] 

    return country_codpos,province_codpos,charge_shipment_codpos

def calculate_shipment(charge_shipment,type_shipment,waypay):
    type_shipment_cost_tup = (1100,1800,2450,8300,10900,14300,17900)
    waypay_tup = (0.9,1) # 1 = pago en Efectivo ; 2 = Pago Tarjeta 
    
    cost_shipment = int(type_shipment_cost_tup[type_shipment] * waypay_tup[waypay-1] * charge_shipment)

    return cost_shipment

def valid_address(address_line):
    
    char_ant = '1'

    flg_digits = flg_char = flag_word_digit= False

    for char in address_line:
        
        if not('a' <= char.lower() <= 'z' or '0' <= char <= '9' or char in ('.',' ')): # Busqueda de caracteres especiales
            return False
        
        elif char != ' ' and char != '.':
            
            if 'A' <= char <= 'Z' and 'A' <= char_ant <= 'Z': # Busqueda de mayusculas seguidas
                return False
    
            elif 'a' <= char.lower() <= 'z':
                flg_char = True
            elif '0' <= char <= '9':
                flg_digits = True
        else:      
            if flg_digits and not flg_char:
                flag_word_digit = True
            flg_digits = flg_char = False
        char_ant = char
    
    if  flag_word_digit:
        return True
    else:
        return False
    
def max_type_shipment(simple_letter, registered_letter, express_letter):
    type_shipment_tup = ('Carta Simple','Carta Certificada','Carta Expresa')
    if  simple_letter > registered_letter:
        if simple_letter > express_letter:
            type_max = 0
        else:
            type_max = 2
    elif registered_letter > express_letter:
        type_max = 1
    else:
        type_max = 2
    return type_shipment_tup[type_max]

def print_result(control,cedvalid,cedinvalid,imp_acu_total,ccs,ccc,cce,tipo_mayor,primer_cp,cant_primer_cp,menimp,mencp,porc,prom):
     
     print(' (r1) - Tipo de control de direcciones:', control)
     print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
     print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
     print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
     print(' (r5) - Cantidad de cartas simples:', ccs)
     print(' (r6) - Cantidad de cartas certificadas:', ccc)
     print(' (r7) - Cantidad de cartas expresas:', cce)
     print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
     print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
     print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
     print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
     print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
     print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
     print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)