## Soporte para JSON en Python
import json
str_json_data = "{\"x\":5, \"y\":6}"
data = json.loads( str_json_data )
print (data)
print (data["x"])

# Cambio en x
data["x"] = 100
print( "Cambio de x de 5 a 100: ")
print( data )

# Volver a JSON
print( "Devolver a JSON: " )
print( json.dumps( data ) )
