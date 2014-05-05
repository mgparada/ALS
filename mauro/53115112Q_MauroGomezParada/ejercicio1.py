__author__ = 'mauro'

## Ejercicio 1
def es_palindromo(cadena):
    lista = []
    for i in cadena:
        lista.append(i)

    cont = 0
    ok = True
    for i in cadena[::-1]:
        if lista[cont] == i:
                cont += 1
        else:
            ok = False


    if ok :
        print("La cadena es un palindromo")
    else:
        print("La cadena no es un palindromo")

print ("--- Ejercicio 1 ---")
es_palindromo("casa")
es_palindromo("radar")
