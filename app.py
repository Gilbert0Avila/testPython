
from clases import CTratarTexto 
from sources import  inputs
from clases import  CManejoDeDatos

def solicitarDatos(objData):
    nameData = input("Nombre Directorio:")
    name = input("name:")
    level = input("level:")
    priority = input("priority:")
    newData = {nameData: {
            "name": name,
            "level": level,
            "priority": priority
        }}
    objDatos = CManejoDeDatos.CManejoDeDatos()
    return objDatos.insertarDatos(objData,newData)
    
def insertarData(objData):
    objDatos = CManejoDeDatos.CManejoDeDatos()
    print("**********************************")
    print(objDatos.show(objData,0))
    print("*1-insertar en principal*")
    keys = list(objData.keys())
    cont = 1
    for key in keys:
        
        if key not in ("name","level","priority"):
            cont = cont+1
            print("*"+str(cont)+"-insertar en "+str(key)+"*")
    opcion = input("*Seleccione una opcion:")
    match opcion:
        case "1":
           objData= solicitarDatos(objData)
        case default:
            if(int(opcion)<cont):
                print(cont)
                objData[keys[int(opcion)-2]]= insertarData(objData[keys[int(opcion)-2]])
            else:
               objData =  insertarData(objData)

            
    return objData
    
def manejoDeDatos():
    objDatos = CManejoDeDatos.CManejoDeDatos()
    print("**********************************")
    print("*1- Ordenar y mostrar Datos      *")
    print("*2- insertar                     *")
    opcion = input("*ingrese una opcion*:\n")
    match opcion:
        case "1":
            dataTemp = objDatos.ordenamiento(inputs.data)
            print(objDatos.show(dataTemp,0))
            return True
        case "2":
            inputs.data = insertarData(inputs.data)
            print(inputs.data)
            
def vocales():
    objTexto = CTratarTexto.CTratarTexto()
    cadena = input("ingresa una frase:\n")
    dat = objTexto.contar_vocales(cadena)
    print('la cadena "'+str(cadena) +'" tiene '+str(dat["contador"]) + ' vocales y si reemplazamos vocales quedaría así "' + dat["cadena"]+'"')



def main():
   while True:
        print("************************")
        print("*1-reemplazar vocales  *")
        print("*2-Manejo de datos     *")
        opcion = input("*ingrese una opcion*:\n")
        match opcion:
            case "1":
                vocales()
            case "2":
                manejoDeDatos()
    

if __name__ == '__main__':
    main()
