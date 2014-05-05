__author__ = 'mauro'

## Ejercicio 2
def histograma(lista):
    for i in lista:
        if i >= 11:
            show = "* * * * * * * * * * *"
            print (str.format("{0} -> {1}", show, str(i)))
        else:
            cont = 0
            show = "*"
            while cont != i:
                show += " *"
                cont += 1

            print (str.format("{0} -> {1}", show, str(i)))


print ("--- Ejercicio 2 ---")
histograma([1, 2, 3, 13, 400])
