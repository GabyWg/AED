import register as reg
from os import system
import os.path
import pickle
import csv


def text_menu(): #Funcion donde contenemos el menu
    text='''
1- Load shipping data by comma delimited file.
2- Load shipping data by keyboard.
3- Show shipping data.
4- Search for shipments - By Postal Code.
5- Search for shipments - By Address.
6- Quantity of shipments by type of shipment and type of payment (Matrix).
7- Quantity of shipments by type of shipment and type of payment (By category) (The results need to be printed correctly.)
8- Shipping type data with the highest amount. (It remains to be finished.)
0- Program exit.
Select an option: '''
    return text


def number_valid(min_num,max_num,sms): # Para validar el ingreso de numeros
    n = input(sms)
    digit_flg = False if isdigit(n) == True else True
    while digit_flg or (min_num > int(n) or int(n) > max_num):
        system("cls")
        print(f'Invalid option.')
        n = input(sms)
        digit_flg = False if isdigit(n) == True else True

    return int(n)


def load_data_binary_shipment(arch_name_csv,arch_name_binary): # Para crear un archivo binario en base a un archivo csv
    arch_csv = main_arch(arch_name_csv,'rt')
    answer = 1
    if arch_csv is not None:
        arch_binary = main_arch(arch_name_binary,'wb')
        if  arch_binary is not None:
            answer = number_valid(0,1,f"You have shipping data loaded, if you continue they will be deleted.\n0- Cancel operation.\n1- Continue.\nSelect an option: ")
            if answer == 0:
                return print("Canceled Operation.")
        for text_line in arch_csv:
            ship_data = analyze_line(text_line.replace('\n',''))
            if  ship_data is None:
                pass
            else:
                pickle.dump(ship_data,arch_binary)
        main_arch('-1', '-1', False, [arch_csv,arch_binary])   #Cierra el archivo.
        print(f"Data were loaded.")


def load_data_keyboard_shipment(arch_name_binary): # Para cargar datos via ingreso de teclado
    cod_pos_flg = address_flg = type_shipment_flg = waypay_flg = True
    sms = '0- Enter data again.\n1- Continue.\nSelect an option: '

    ################################################################################################

    while cod_pos_flg:
        cod_pos = input('Enter the postal code: ')
        country_shipment,province_shipment,charge_shipment = analyze_codpos(cod_pos)
        system("cls")
        print(f'The postal code entered is: {cod_pos}\n'
              f'Postal code Country: {country_shipment}\n'
              f'Postal code province: {province_shipment}\n'
              f'Postal code shipping charge: {charge_shipment}\n')
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            cod_pos_flg = False
    system("cls")
    ################################################################################################

    while address_flg:
        address = input('Enter the address: ')
        system("cls")
        print(f'The address entered is: {address}\n')
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            address_flg = False
    system("cls")
    ################################################################################################

    while type_shipment_flg:
        id_type_shipment = number_valid(0,6,'Enter the shipping type between values ​​0 and 6: ')
        system("cls")
        print(f'The shipping type entered is: {id_type_shipment}')
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            type_shipment_flg = False
    system("cls")
    ################################################################################################

    while waypay_flg:
        waypay = number_valid(1,2,'Enter the shipping type between values 1(Cash) and 2(Credit Card): ')
        system("cls")
        print(f'The shipping type entered is: {waypay}')
        number_flg = number_valid(0,1,sms)
        if number_flg == 1:
            waypay_flg = False
    system("cls")
    ################################################################################################

    cost_shipment = calculate_shipment(charge_shipment,id_type_shipment,waypay)

    ship_data = reg.Envio(cod_pos,address,id_type_shipment,waypay,cost_shipment,country_shipment,province_shipment)
    
    arch_binary = main_arch(arch_name_binary,'ab')
    pickle.dump(ship_data,arch_binary)
    main_arch('-1', '-1', False, [arch_binary])

    print(f"Se agregaron los siguientes datos de envio.\n{ship_data}")

def main_arch(name_arch, mode, flg_open = True, arch = None): #Funcion que abre el archivo que se le envia, al finalizar la lectura se le enviar otros parametros de otra funcion para cerrar el mismo
    
    if flg_open:
        if mode[0] == 'r':
            if  os.path.exists(name_arch):
                return open(name_arch,mode)
            else:
                print(f'El archivo {name_arch} no existe.')
                return None
        else:
            return open(name_arch,mode)
    else:
        (arch.close() for arch in range(len(arch)))


def analyze_line (text_line): # Funcion principal, analiza toda la linea de envio
    ship_data = None
    text_data = text_line.split(',')
    if len(text_data) == 4 and str(text_data[0].strip()) != 'codigo_postal':
        codpos_line,address_line,id_type_shipment_line,waypay_line = str(text_data[0].strip()),str(text_data[1].strip()),int(text_data[2]),int(text_data[3]) 
        country_shipment,province_shipment,charge_shipment = analyze_codpos(codpos_line)
        cost_shipment = calculate_shipment(charge_shipment,id_type_shipment_line,waypay_line)
        ship_data = reg.Envio(codpos_line,address_line,id_type_shipment_line,waypay_line,cost_shipment,country_shipment,province_shipment)

    return ship_data


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


def print_shipments(arch_name_binary,type_show='All',filter='-1'):
    arch_binary = main_arch(arch_name_binary,'rb')
    tam_arch = os.path.getsize(arch_name_binary)
    count_print = 0

    if type_show == 'All':
        while arch_binary.tell() < tam_arch:
            print(pickle.load(arch_binary)) 

    elif type_show == 'codpos':
        while arch_binary.tell() < tam_arch:
            ship_data = pickle.load(arch_binary)
            if ship_data.cod_pos == filter:
                count_print +=0
                print(ship_data)
        print(f"Registros mostrados: {count_print}")
    
    main_arch('-1', '-1', False, [arch_binary])
 

def search_adress(arch_name_binary,adress_search):
    
    arch_binary = main_arch(arch_name_binary,'rb')
    tam_arch = os.path.getsize(arch_name_binary)
    ship_search = None
    while arch_binary.tell() < tam_arch:
        ship_data = pickle.load(arch_binary)
        if ship_data.address == adress_search:
            ship_search = ship_data
            break

    main_arch('-1', '-1', False, [arch_binary])
    return ship_search


def shipment_count_type(arch_name_binary):
    mat_result = [[0]*2  for i in range(7)]
    
    arch_binary = main_arch(arch_name_binary,'rb')
    tam_arch = os.path.getsize(arch_name_binary)
    ship_search = None
    while arch_binary.tell() < tam_arch:
        ship_data = pickle.load(arch_binary)
        mat_result[ship_data.type_shipment][ship_data.waypay-1]  += 1  

    main_arch('-1', '-1', False, [arch_binary])

    return mat_result


def print_count_mat(result_count):
    count_type_shipment = [0]*7
    count_waypay = [0]*2
    for i in range(len(result_count)):
        for j in range(len(result_count[i])):
            count_type_shipment[i] += result_count[i][j]
            count_waypay[j] += result_count[i][j]
    print(count_type_shipment)
    print(count_waypay)


def order_min_to_max_codpos(v_envios):
    len_vec = len(v_envios)
    div = len_vec//2

    while div > 0:
        for i in range(div,len_vec):
            temp = v_envios[i]
            j = i

            while j >= div and v_envios[j - div].cod_pos > temp.cod_pos:
                v_envios[j] = v_envios[j - div]
                j -= div
            v_envios[j] = temp
        div //= 2