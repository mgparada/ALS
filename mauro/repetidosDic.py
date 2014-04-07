## Contar elementos lista usando diccionario

def numOcurrencias(lista, num, myDic):
    numOcurr = 0
    for item in lista:
        if(item == num):
            numOcurr += 1
            
    if numOcurr > 1:
        myDic[num]  = numOcurr

def repetidos(lista, myDic):
    for item in lista:
        numOcurrencias(lista, item, myDic)
    
    return myDic

def main():
    lista = [1, 2, 2, 3, 3, 3, 4, 5, 5, 4, 3, 5]
    myDic = {}
    myDic = repetidos(lista, myDic)
    print(myDic)
    
main()