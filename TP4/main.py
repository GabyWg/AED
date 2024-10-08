import functions as func

CSV_ARCH = 'envios-tp4.csv'
BINARY_ARCH = "envios-tp4.dat"



def main():

    turns = True
    flg_six = False

    while turns:
        value_option = func.number_valid(0, 8, func.text_menu())

        if value_option == 1:

            func.load_data_binary_shipment(CSV_ARCH, BINARY_ARCH)

        elif value_option == 2:
            func.load_data_keyboard_shipment(BINARY_ARCH)

        elif value_option == 3:
            func.print_shipments(BINARY_ARCH)

        elif value_option == 4:
            codpos_search = input("Enter an zip code to search: ")

            func.print_shipments(BINARY_ARCH, 'codpos', codpos_search)

        elif value_option == 5:
            adress_search = input("Enter an address to search (Do not put the final point): ") + '.'

            result_search = func.search_adress(BINARY_ARCH, adress_search)

            if result_search is None:
                print("No results found.")
            else:
                print(f"A match was found.\n{result_search}")

        elif value_option == 6:
            result_count = func.shipment_count_type(BINARY_ARCH)
            print("Quantity of shipments by type of shipment.")
            for i in range(len(result_count)):
                print(f"Shipment type {i}")
                for j in range(len(result_count[i])):
                    if result_count[i][j] != 0:
                        print(f"   Waypay {j + 1}: {result_count[i][j]}")
            flg_six = True

        elif value_option == 7:
            if flg_six:
                func.print_count_mat(result_count)
            else:
                print("Please, this point depends on option 6.\nExecute point 6.")

        elif value_option == 8:
            vector = list()
            func.generate_order_array(BINARY_ARCH, vector)
            func.order_min_to_max_codpos(vector)
            func.show_vector(vector)

        elif value_option == 0:
            turns = False
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()