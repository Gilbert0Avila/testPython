class CTratarTexto:
    global arrVocales
    def __init__(self):
      self.arrVocales = ("a","e","i","o","u","a","A","E","I","O","U","A")
      

    def contar_vocales(self,cadena):
        datRet = {"contador":0,"cadena":""}
        cadenaRet = ""
        contador = 0
        for letra in cadena:
            if letra in self.arrVocales:
                contador += 1
                letra = self.reemplazarVocales(letra)
            cadenaRet=cadenaRet+letra
        
        datRet["contador"] = contador
        datRet["cadena"] = cadenaRet
        return datRet
    
    def reemplazarVocales(self,vocal):
        siguiente = ""
        encontrado = False
        for temp in self.arrVocales:
            if encontrado:
                siguiente = temp
                break
            else:
                if temp == vocal:
                    encontrado = True

             


        return siguiente
         