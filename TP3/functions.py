import register as reg

def text_menu(): #Funcion donde contenemos el menu
    text="""
1- Cargar datos de envios por archivo de texto.
2- Cargar datos de envios por teclado.
3- Mostrar datos de los envios.
4- Busqueda de envios - Por Direccion y Tipo de Envio.
5- Busqueda de envios - Por Codigo Postal.
6- Cantidad de Envios.
7- Importe final de Envios.
8- Datos tipo de envio con mayor importe.
9- Importe final promedio.
0- Salida del programa.
Select an option: """
    return text

def number_valid(min_num,max_num,sms): # Para validar el ingreso de numeros
    n = int(input(sms))
    while min_num > n or n > max_num:
        print("Invalid option, select one of the available options.")
        n = int(input(sms))
    return n  


def start_classes(v_envios=None,v_datashipment=None): # Para iniciar o resetear los vectores que contienen las clases
    v_envios = []
    v_datashipment = []

    return v_envios,v_datashipment


def load_data_text_shipment(v_ship,v_data,arch_name):
    arch_text = main_arch(arch_name) 
    type_control = None

    # while text_line != '' :
    for text_line in arch_text:
        if type_control == None:
            type_control = search_type_control(text_line)
        else:
            analyze_line(text_line,type_control,v_ship,v_data)
        
    main_arch('-1', False, arch_text)   #Cierra el archivo.

def load_data_keyboard_shipment(v_ship,v_data):
    cod_pos_flg = address_flg = type_shipment_flg = waypay_flg = True
    sms = "0- Enter data again.\n1- Continue.\nSelect an option: "
    struct_control = ''

################################################################################################
    while cod_pos_flg:
        cod_pos = input("Enter the postal code: ")
        country_shipment,province_shipment,charge_shipment = analyze_codpos(cod_pos)
        print(f"The postal code entered is: {cod_pos}\n"
              f"Postal code Country: {country_shipment}\n"
              f"Postal code province: {province_shipment}\n"
              f"Postal code shipping charge: {charge_shipment}\n")
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            cod_pos_flg = False
################################################################################################
    while address_flg:
        address = input("Enter the address: ")
        while struct_control != 'HC' and struct_control != 'SC':
            struct_control = input("Enter shipping struct HC(Hard Control) or SC(Soft Control): ").upper()
            address_valid = True if 'SC' == struct_control else valid_address(address) 
        print(f"The address entered is: {address}\n"
            f"Type of shipment entered: {struct_control}\n")
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            address_flg = False
################################################################################################
    while type_shipment_flg:
        id_type_shipment = number_valid(0,6,"Enter the shipping type between values ​​0 and 6: ")
        print(f"The shipping type entered is: {id_type_shipment}")
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            type_shipment_flg = False
################################################################################################
    while waypay_flg:
        waypay = number_valid(1,2,"Enter the shipping type between values 1(Cash) and 2(Credit Card): ")
        print(f"The shipping type entered is: {waypay}")
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            waypay_flg = False
################################################################################################

    cost_shipment = calculate_shipment(charge_shipment,id_type_shipment,waypay)

    v_ship.append(reg.Envio(cod_pos,address,id_type_shipment,waypay))
    v_data.append(reg.DataShipment(cost_shipment,address_valid,country_shipment,province_shipment)) # Construction is desc_type_shipment


def main_arch(name_text, flg_open = True, arch = None): #Funcion que abre el archivo que se le envia, al finalizar la lectura se le enviar otros parametros de otra funcion para cerrar el mismo
    if flg_open:
        arch = open(name_text,'rt')
        return arch
    else:
        arch.close()


def search_type_control(line_text): # Recibe una linea de texto y revisa que tipo de control es el indicado
    return 'Hard Control' if 'HC' in line_text.upper() else 'Soft Control'


def analyze_line (text_line,control,v_ship,v_data): # Funcion principal, analiza toda la linea de envio (codigo postal, )

    codpos_line,address_line,id_type_shipment_line,waypay_line = text_line[:9].strip(),text_line[9:29].strip(),int(text_line[29]),int(text_line[30]) 
    
    country_shipment,province_shipment,charge_shipment = analyze_codpos(codpos_line)
    
    cost_shipment = calculate_shipment(charge_shipment,id_type_shipment_line,waypay_line)
    
    address_valid = True if 'Soft Control' == control else valid_address(address_line) 

    v_ship.append(reg.Envio(codpos_line,address_line,id_type_shipment_line,waypay_line))
    v_data.append(reg.DataShipment(cost_shipment,address_valid,country_shipment,province_shipment)) # Construction is desc_type_shipment


def analyze_codpos(cod_pos): # Analiza el codigo postal, devuelve Pais, provincia y cargo del envio

    letter_tup = ('B', 'C', 'K', 'H', 'U', 'X', 'W', 'E', 'P', 'Y', 'L', 'F', 'M', 'N', 'Q', 'R', 'A', 'J', 'D', 'Z', 'S', 'G', 'V', 'T')

    prov_tup = ('Provincia de Buenos Aires', 'Ciudad Autónoma de Buenos Aires', 'Catamarca', 'Chaco',
                    'Chubut', 'Córdoba', 'Corrientes','Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa','La Rioja', 
                    'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz',
                    'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán')
    
    cod_pos = cod_pos.upper()

    large_codpos = len(cod_pos)

    if isdigit(cod_pos):
        if large_codpos == 4:
            country_codpos = 'Bolivia'
            charge_shipment_codpos = 1.20
        elif large_codpos == 5:
            country_codpos = 'Uruguay'
            charge_shipment_codpos = 1.2 if cod_pos[0] == '1'  else 1.25
        elif large_codpos == 6:
            country_codpos = 'Paraguay'
            charge_shipment_codpos = 1.20
        elif large_codpos == 7:
            country_codpos = 'Chile'
            charge_shipment_codpos = 1.25
        else:
            country_codpos = 'Otro'
            charge_shipment_codpos = 1.5
    else:
        if large_codpos == 8:
            if not(isdigit(cod_pos[0] + cod_pos[5:8])) and isdigit(cod_pos[1:5]):
                if not(cod_pos[0].upper() in ('I','O') ):
                    country_codpos = 'Argentina'
                    charge_shipment_codpos = 1
                else:
                    country_codpos = 'Otro'
                    charge_shipment_codpos = 1.5
            else:
                country_codpos = 'Otro'
                charge_shipment_codpos = 1.5
        
        elif large_codpos == 9 and cod_pos[5] == '-' and isdigit(cod_pos.replace('-', '')):
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


def isdigit(text): # Saber si un conjunto de caracteres son todos digitos
    flg = True
    text = str(text)
    for char in text:
        if not('0' <= char <= '9'):
            flg = False
    return flg


def calculate_shipment(charge_shipment,type_shipment,waypay): # Calcula el total del costo del envio, 
    type_shipment_cost_tup = (1100,1800,2450,8300,10900,14300,17900)
    waypay_tup = (0.9,1) # 1 = pago en Efectivo ; 2 = Pago Tarjeta 
    
    cost_shipment = int(int(type_shipment_cost_tup[type_shipment] * charge_shipment) *   waypay_tup[waypay-1])

    return cost_shipment

def valid_address(address_line): # Validacion de la direccion
    
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


# def max_type_shipment(simple_letter, registered_letter, express_letter): # Me calcula el maximo de cantidad de los tipos de cartas y me devuelve el nombre del mismo
#     type_shipment_tup = ('Carta Simple','Carta Certificada','Carta Expresa')
#     if  simple_letter > registered_letter:
#         if simple_letter > express_letter:
#             type_max = 0
#         else:
#             type_max = 2
#     elif registered_letter > express_letter:
#         type_max = 1
#     else:
#         type_max = 2
#     return type_shipment_tup[type_max]

# def calculate_porc_inter(count_shipment,valid_shipment): # calcula el porcentaje de los envios internacionales sobre los totales
#     if valid_shipment == 0:
#         return 0
#     else:
#         return int((count_shipment*100)/valid_shipment)

# def calculate_avg_bsas(sum_import,count_shipment): # calcula el promedio del costo de envios a bs as
#     if count_shipment == 0:
#         return 0
#     else:
#         return int(sum_import/count_shipment)