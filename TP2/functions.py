def hola():
    pass

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
    codpos_line,address_line,type_shipment_line,waypay_line = text_line[:9],text_line[9:29],text_line[29],text_line[30]  
    
    address_flg = True if 'Soft Control' == control else valid_address(address_line)
    
    return address_flg

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

def print_result(control,cedvalid,cedinvalid):
     
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