__author__ = 'Walter Gabriel Garay'

def principal():
    #number_sum = number_count =  0 Aguanten las listas
    number_may = number_succession = int(input("Ingrese un numero para la sucesion: "))
    list_number = []

    list_number.append(number_succession)
    while number_succession != 1:

        if number_succession > number_may:
            number_may = number_succession

        number_succession = sucesion_func(number_succession )
        list_number.append(number_succession)

    print(f"n = {number_succession} \n"
        f"Orbita de n = {number_succession} (valores calculados incluyendo al 13 y al 1): {list_number} \n"
        f"Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): {len(list_number)} \n"
        f"Promedio de todos los valores de la órbita: {round(sum(list_number)/len(list_number),1)} \n"
        f"Mayor de los números en esa órbita: {number_may} \n")

def sucesion_func(number):
    if number % 2 == 0:
        return int(number/2)
    else:
        return int(number*3 + 1)
    
if __name__ == '__main__':
    principal()