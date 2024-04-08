import pandas as pnd
import json

with open('Dia_3/data.json','r') as p:
    data = json.load(p)

tabla = pnd.DataFrame(data)

with open('Dia_3/index.html','a') as f:
    f.write(tabla.to_html(index=False))    

