import functions as func

##### ARCHIVOS DE PRUEBA (DEJAR COMENTADO)
NAME_TEXT = 'envios25.txt'

arch_text = func.main_arch(NAME_TEXT) # Si podemos trabajar de esta forma el archivo !! 

def main_main():
    for arch in arch_text:
        print(arch, end='')

if __name__ == "__main__":
    main_main()
