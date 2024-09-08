import functions as func
import register as reg
from os import system

NAME_TEXT = 'envios-tp3.txt'
#NAME_TEXT = 'envios-tp3-prueba.txt'

def main():
    #Inicializacion de Variables
    turns = True
    value_option = 0
    v_envios = func.start_classes()
    option_8 = False
    while turns:
        value_option = func.number_valid(0,9,func.text_menu())
        system("cls") 
        if len(v_envios) == 0 and value_option > 1:
            print("""There is no shipping data loaded to continue.
                  Please select option 1.""")
        else:
            if value_option == 1:
                if len(v_envios) == 0:
                    type_struct = func.load_data_text_shipment(v_envios,NAME_TEXT) # Carga de archivos y regresa el tipo de timestamp
                    print(f"{len(v_envios)} data were loaded.")
                
                else:
                    answer = func.number_valid(0,1,f"You have {len(v_envios)} shipping data loaded, if you continue they will be deleted.\n0- Cancel operation.\n1- Continue.\nSelect an option: ")
                    if answer == 1:
                        v_envios = func.start_classes()
                        type_struct = func.load_data_text_shipment(v_envios,NAME_TEXT) # Carga de archivos
                        print(f"{len(v_envios)} data were loaded.")
                    
                    else:
                        print("Canceled Operation.")

            elif value_option == 2:
                func.load_data_keyboard_shipment(v_envios,type_struct)
            
            elif value_option == 3:
                func.order_min_to_max_codpos(v_envios)
                option_list = func.number_valid(0,1,"Do you want to see the full list?\n0- Yes.\n1- No.\nSelect an option: ")
                if option_list == 0:
                    func.print_shipments(v_envios)
                else:
                    func.print_shipments(v_envios,type_show='firts_n_ships',quan_row=func.number_valid(1,len(v_envios),"Enter the number of rows to display: "))
            
            elif value_option == 4:
                adress_search = input("Enter an address to search (Do not put the final point): ") + '.'
                
                type_shipment_search = func.number_valid(0,6,"Enter the shipping type: ")
                
                result_search = func.search_adress(v_envios,adress_search,type_shipment_search)

                if result_search is None:
                    print("No results found.")
                else:
                    print(f"A match was found.\n{result_search}")
            
            elif value_option == 5:
                codpos_search = input("Enter an zip code to search: ")
                                
                result_search = func.search_codpos(v_envios,codpos_search)

                if result_search is None:
                    print("No results found.")
                else:
                    print(f"A match was found.\n{result_search}")
            
            elif value_option == 6:
                result_count = func.shipment_count_type(v_envios)
                print("Quantity of shipments by type of shipment.")
                for i in range(len(result_count)):
                    print(f"Shipment type {i}: {result_count[i]}")
            
            elif value_option == 7:
                sum_import_type, full_import= func.shipment_sum_import_type(v_envios)
                print("Total import by shipment type.")
                for i in range(len(sum_import_type)):
                    print(f"Shipment type {i}: {sum_import_type[i]}")
                option_8 = True
                
            elif value_option == 8:
                if option_8:
                    porc_import_type = func.calc_porc_type_ship(sum_import_type,full_import)
                    print("Percentage of the total by type of shipment..")
                    for i in range(len(porc_import_type)):
                        print(f"Shipment type  {i}: {porc_import_type[i]}%")
                else:
                    print("Please, this point depends on option 7.\nExecute point 7.")
            
            elif value_option == 9:
                avg_shipment = round(func.avg_shipment_cost(v_envios),2)
                print(f"The average per shipment is: $ {avg_shipment}")
                min_avg_cost_shipment = func.count_ship_avg_min_cost(v_envios,avg_shipment)
                print(f"The number of shipments with a cost lower than the average is: {min_avg_cost_shipment}")

            else: #Unico valor disponible sera el 0.
                break
        input("Press enter to continue.")
        system("cls")

if __name__ == "__main__":
    main()