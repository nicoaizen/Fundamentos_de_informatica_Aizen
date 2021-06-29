import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas')
r.json()

>>> r.json()
[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}, {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, {'id': 17, 'tipo': 'saco', 'talle': 'S'}, {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, {'id': 19, 
'tipo': 'saco', 'talle': 'L'}, {'id': 20, 'tipo': 'saco', 'talle': 'XL'}]

>>> r.content
b'[\n  {\n    "id": 1,\n    "tipo": "pantalon",\n    "talle": 35\n  },\n  {\n    "id": 2,\n    "tipo": "pantalon",\n    "talle": 36\n  },\n  {\n    "id": 3,\n    "tipo": "pantalon",\n    "talle": 37\n  },\n  {\n    "id": 4,\n    "tipo": "pantalon",\n    "talle": 38\n  },\n  {\n    "id": 5,\n    "tipo": "pantalon",\n    "talle": 39\n  },\n  {\n    "id": 6,\n    "tipo": "pantalon",\n    "talle": 40\n  },\n  {\n    "id": 7,\n    "tipo": "pantalon",\n    "talle": 41\n  },\n  {\n    "id": 8,\n    "tipo": "pantalon",\n    "talle": 42\n  },\n  {\n    "id": 9,\n    "tipo": "pantalon",\n    "talle": 43\n  },\n  {\n    "id": 10,\n    "tipo": "pantalon",\n   
 "talle": 44\n  },\n  {\n    "id": 11,\n    "tipo": "remera",\n    "talle": "XS"\n  },\n  {\n    "id": 12,\n    "tipo": "remera",\n    "talle": "S"\n  },\n  {\n    
"id": 13,\n    "tipo": "remera",\n    "talle": "M"\n  },\n  {\n    "id": 14,\n    
"tipo": "remera",\n    "talle": "L"\n  },\n  {\n    "id": 15,\n    "tipo": "remera",\n    "talle": "XL"\n  },\n  {\n    "id": 16,\n    "tipo": "saco",\n    "talle": "XS"\n  },\n  {\n    "id": 17,\n    "tipo": "saco",\n    "talle": "S"\n  },\n  {\n    "id": 18,\n    "tipo": "saco",\n    "talle": "M",\n    "enStock": false\n  },\n  {\n    "id": 19,\n    "tipo": "saco",\n    "talle": "L"\n  },\n  {\n    "id": 
20,\n    "tipo": "saco",\n    "talle": "XL"\n  }\n]'

>>> import requests
>>> r = requests.get('https://macowins-server.herokuapp.com/ventas')
>>> r.json()

>>> import requests
>>> r = requests.get('https://macowins-server.herokuapp.com/ventas/2')
>>> r.json()

#La diferencia entre las dos es que "/ventas" muestra todas las ventas
#registradas, mientras que "ventas/2" unicamente muestra la venta con
#"id" : 2

>>> r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon')
>>> r.json()

>>> r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
>>> r.json()
[
  {
    "id": 11,
    "tipo": "remera",
    "talle": "XS"
  },
  {
    "id": 12,
    "tipo": "remera",
    "talle": "S"
  },
  {
    "id": 13,
    "tipo": "remera",
    "talle": "M"
  },
  {
    "id": 14,
    "tipo": "remera",
    "talle": "L"
  },
  {
    "id": 15,
    "tipo": "remera",
    "talle": "XL"
  }
]

>>> import requests
>>> r = requests.get("https://macowins-server.herokuapp.com/prendas?talle=XS&tipo=remera")
>>> r.json()
[{'id': 11, 'tipo': 'remera', 'talle': 'XS'}]