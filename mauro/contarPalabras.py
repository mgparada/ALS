## Contar elementos lista de palabras usando diccionario

def repetidos(cadena, myDic):
    lista = cadena.strip().split()
    for item in lista:
        if myDic.get(item) != None:
            myDic[item] += 1
        else:
                myDic[item] = 1
    
    return myDic

def main():
    cadena = "el perro de la huerta marron es marron"
    myDic = {}
    myDic = repetidos(cadena, myDic)
    print(myDic)
    
main()