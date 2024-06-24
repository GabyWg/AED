import functions as func

#PARA REVISAR LOS CAMBIOS QUE SE HAN REALIZADO DESPUES DE LA NOTA BUSCAR -> 'Cod_Revisar'

##### ARCHIVOS DE PRUEBA (DEJAR COMENTADO)
#NAME_TEXT = 'envios25.txt'
# NAME_TEXT = 'envios100SC.txt'
# NAME_TEXT = 'envios100HC.txt'

##### ARCHIVO PARA LA CORRIDA DEL TP2 (DESCOMENTAR !!!!!!!!!!!!) DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR DESCOMENTAR
#NAME_TEXT = 'envios.txt'
NAME_TEXT = 'envios500b.txt'

def principal ():
    control_r1 = None #RTA_1
    invalid_shipment = valid_shipment = 0 #RTA_2_3
    import_valid_shipment = import_invalid_shipment = 0 #RTA_4
    simple_letter_valid = registered_letter_valid = express_letter_valid = 0 #RTA_5_6_7
    simple_letter_invalid = registered_letter_invalid = express_letter_invalid = 0 #RTA_5
    firts_codpos = None #RTA_9
    count_firts_codpos = 1 #RTA_10
    min_import_br = None # RTA_11
    codpos_min_import_br = None # RTA_12
    count_inter_shipment = 0 #RTA_13
    sum_import_bsas = count_shipment_bsas =  0 #RTA_14


    arch_text = func.main_arch(NAME_TEXT) # Si podemos trabajar de esta forma el archivo !! 

    # text_line = func.read_line(arch_text)

    # while text_line != '' :
    for text_line in arch_text:
        if control_r1 == None:
            control_r1 = func.type_control(text_line)
        else:
            address_flg,import_shipment,id_type_shipment,codpos_shipment,country_shipment,province_shipment = func.analyze_line(text_line,control_r1)

            if firts_codpos == None:
                firts_codpos = codpos_shipment
            else:
                if firts_codpos == codpos_shipment:
                    count_firts_codpos +=1

            if country_shipment == 'Brasil':
                if min_import_br == None or min_import_br > import_shipment:
                    min_import_br = import_shipment
                    codpos_min_import_br = codpos_shipment

            if address_flg: # Envio Valido
                valid_shipment += 1
                import_valid_shipment += import_shipment

                if country_shipment not in ('Argentina'): # Buscamos que sea un envio exterior
                    count_inter_shipment += 1
                else:
                    if province_shipment == 'Provincia de Buenos Aires':
                        #Antes del cambio ->  sum_import_bsas =+ import_shipment     Cod_Revisar
                        sum_import_bsas += import_shipment
                        count_shipment_bsas += 1

                if 0 <= id_type_shipment <= 2:
                    simple_letter_valid +=1
                elif 3 <= id_type_shipment <= 4:
                    registered_letter_valid +=1
                elif 5 <= id_type_shipment <= 6:
                    express_letter_valid +=1

            else:   # Envio No Valido   
                invalid_shipment += 1
                import_invalid_shipment += import_shipment

                # NO HACEN FALTA LOS TIPOS DE CARTAS CON DIRECCION INVALIDA
                # if 0 <= id_type_shipment <= 2:
                #     simple_letter_invalid +=1
                # elif 3 <= id_type_shipment <= 4:
                #     registered_letter_invalid +=1
                # elif 5 <= id_type_shipment <= 6:
                #     express_letter_invalid +=1

        # text_line = func.read_line(arch_text)
        
    func.main_arch('-1', False, arch_text)  

    max_shipment_type = func.max_type_shipment(simple_letter_valid, registered_letter_valid, express_letter_valid) # RTA_8
    #porc_inter_shipment = func.calculate_porc_inter(count_inter_shipment,valid_shipment )#  +invalid_shipment )  #RTA_13 Antes del Cambio Cod_Revisar
    porc_inter_shipment = func.calculate_porc_inter(count_inter_shipment,valid_shipment   +invalid_shipment )  #RTA_13

    # Si sigo la consigna del Punto 13, no me dan los resultados de ninguno de los Hard Control //
    # pero si sumo los pedidos invalidos e validos si me dan los resultados ### Por ahora lo dejaremos tal cual la consigna del 13

    avg_import_bsas = func.calculate_avg_bsas(sum_import_bsas,count_shipment_bsas) #RTA_14

    func.print_result(control_r1, 
                      valid_shipment+invalid_shipment if 'Soft Control' == control_r1 else valid_shipment,
                      0                               if 'Soft Control' == control_r1 else invalid_shipment,
                      import_valid_shipment,
                      simple_letter_valid,
                      registered_letter_valid,
                      express_letter_valid,
                      max_shipment_type,
                      firts_codpos,
                      count_firts_codpos,
                      min_import_br,
                      codpos_min_import_br,
                      porc_inter_shipment,
                      avg_import_bsas
                      )


if __name__ == "__main__":
    principal()
