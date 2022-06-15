class CManejoDeDatos:
    def imprimirData(self,arrData,level):
        keys = list(arrData.keys())
        cadena =""
        for key in keys:
            
            if type(arrData[key])==dict:
                cadena = cadena  + "----"*level+">"+ arrData[key]["name"] +"\n" + self.imprimirData(arrData[key],level+1)
            else:
                pass

        return cadena
   
    def priorizar(self,obj):
        #niveles de prioridad

        arrMaestro ={}
        arrLowest  ={}
        arrLow     ={}
        arrMedium  ={}
        arrHigh    ={}
        arrHighest ={}
        temp = {}
        subData = True
        #print("----------------------")
        for key in list(obj.keys()):
            temp[key] = obj[key]
            if key not in ("name","level","priority"):
                subData = False
                priority = obj[key]["priority"]

                if priority == "Lowest":
                    arrLowest[key]=obj[key]
                elif priority == "Low":
                    arrLow[key]=obj[key]
                elif priority == "Medium":
                    arrMedium[key]=obj[key]
                elif priority == "High":
                    arrHigh[key]=obj[key]
                elif priority == "Highest":                    
                    arrHighest[key]=obj[key]
            else:
                arrMaestro[key] = obj[key]
            
        #se ordenan por prioridad
        arrMaestro.update(arrHighest)
        arrMaestro.update(arrHigh)
        arrMaestro.update(arrMedium)
        arrMaestro.update(arrLow)
        arrMaestro.update(arrLowest)
        if(subData):
            arrMaestro =obj
        return arrMaestro
    
    def ordenamiento(self,obj):
        temp = self.priorizar(obj)
        temp2 ={}
        keys = list(temp.keys())
        for key in keys:
            if key not in("name","level","priority"):
                temp2[key] = self.ordenamiento(temp[key])
            else:
               temp2.update(temp)
                
        return temp2
    