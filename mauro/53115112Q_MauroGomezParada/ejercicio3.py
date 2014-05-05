__author__ = 'mauro'

## Ejercicio 3
def inversa(lista):
    lista_inversa = []
    for i in lista[::-1]:
        lista_inversa.append(i)

    print( str.format("La lista inversa de {0} es {1}", lista, lista_inversa) )


print ("--- Ejercicio 3 ---")
inversa([1, 2, 3, 4, 5, 6])