import json

str_json_sata = "{\"x\":5, \"y\": 6}"

data = json.loads( str_json_sata )
print (data)
print (data["x"])

#Cambiando Json
data["x"] = 100
print ("Cambiando variable X...")
print (data)

# volviendo datos a Json
print ("Devolviendo dic {} en Json")
print (json.dumps(data))