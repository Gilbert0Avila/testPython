from clases import CTratarTexto 
def main():
    # todo: code here
    objTexto = CTratarTexto.CTratarTexto()
    cadena = input("ingresa una frase:\n")
    dat = objTexto.contar_vocales(cadena)

    print('la cadena "'+str(cadena) +'" tiene '+str(dat["contador"]) + ' vocales y si reemplazamos vocales quedaría así "' + dat["cadena"]+'"')
    pass


if __name__ == '__main__':
    main()

