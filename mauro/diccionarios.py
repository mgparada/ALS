## Diccionarios ##

# Maneras de crear un diccionario...
d1 = dict()
d2 = {}

temperaturas = { "Vigo" : 10.5, "Ourense" : 7.2 }

## Acceder al diccionario
print ( temperaturas['Vigo'] )

## Añadir/Modificar valores al diccionario
temperaturas["Oviedo"] = 8.5
print ( temperaturas["Oviedo"] ) 

## Recorrer elementos
for key, value in temperaturas.items():
    print ( key + " : " + str(value))
    
## Acceder a un elemento que no existe
##     Produce excepcion
tempBarcelona = temperaturas.get("Barcelona")
if tempBarcelona != None:
    print ("Barcelona: " + str(tempBarcelona))
else:
    print ("No hay datos para esa ciudad")