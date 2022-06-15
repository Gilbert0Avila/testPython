from sources import  inputs
from clases import  CManejoDeDatos

def main():
    
    
    objDatos = CManejoDeDatos.CManejoDeDatos()
    dataTemp = objDatos.ordenamiento(inputs.data)
    print(objDatos.show(dataTemp,0))
    nameData = input("Nombre data")
    
    newData = {nameData: {
            "name": "One holo",
            "level": "Two",
            "priority": "High"
        }}
    print(newData)
    dataTemp = objDatos.insertarDatos(inputs.data,newData)
    print(objDatos.show(dataTemp,0))

if __name__ == '__main__':
    main()
