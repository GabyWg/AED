import functions as func

NAME_TEXT = 'envios25.txt'
#NAME_TEXT = 'envios100HC.txt'
#NAME_TEXT = 'envios100SC.txt'


def principal ():
    control_r1 = None #RTA_1
    invalid_shipment = valid_shipment = 0 #RTA_2_3
    import_valid_shipment = import_invalid_shipment = 0 #RTA_4
    simple_letter_valid = registered_letter_valid = express_letter_valid = 0 #RTA_5
    simple_letter_invalid = registered_letter_invalid = express_letter_invalid = 0 #RTA_5
    firts_codpos = None #RTA_9
    count_firts_codpos = 1 #RTA_10
    arch_text = func.main_arch(NAME_TEXT)

    text_line = func.read_line(arch_text)

    while text_line != '' :
        if control_r1 == None:
            control_r1 = func.type_control(text_line)
        else:
            address_flg,import_shipment,id_type_shipment,codpos_shipment = func.analyze_line(text_line,control_r1)
            if firts_codpos == None:
                firts_codpos = codpos_shipment
            else:
                if firts_codpos == codpos_shipment:
                    count_firts_codpos +=1
            if address_flg: # Envio Valido
                valid_shipment += 1
                import_valid_shipment += import_shipment
                
                if 0 <= id_type_shipment <= 2:
                    simple_letter_valid +=1
                elif 3 <= id_type_shipment <= 4:
                    registered_letter_valid +=1
                elif 5 <= id_type_shipment <= 6:
                    express_letter_valid +=1

            else:   # Envio No Valido
                invalid_shipment += 1
                import_invalid_shipment += import_shipment

                if 0 <= id_type_shipment <= 2:
                    simple_letter_invalid +=1
                elif 3 <= id_type_shipment <= 4:
                    registered_letter_invalid +=1
                elif 5 <= id_type_shipment <= 6:
                    express_letter_invalid +=1

        text_line = func.read_line(arch_text)

    max_shipment_type = func.max_type_shipment(simple_letter_valid, registered_letter_valid, express_letter_valid) # RTA_8
    
    print(firts_codpos,"-",count_firts_codpos)

    #func.print_result(control_r1, 
    #                  valid_shipment+invalid_shipment if 'Soft Control' == control_r1 else valid_shipment,
    #                  0                               if 'Soft Control' == control_r1 else invalid_shipment 
    #                  import_valid_shipment,
    #                  simple_letter_valid,
    #                  registered_letter_valid,
    #                  express_letter_valid,
    #                  max_shipment_type,
    #                  firts_codpos,
    #                  count_firts_codpos,
    #                  )

if '__name__' == '__name__': 
    principal()
    