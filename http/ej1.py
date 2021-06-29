https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Http_%26_REST/Cloud_Computing_%26_HTTP.md

import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/20')
r.json()

>>> import requests 
>>> r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
>>> r.json()
{'id': 1, 'tipo': 'pantalon', 'talle': 35}
>>> r.headers
{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 'Date': 'Thu, 06 May 2021 14:23:27 GMT', 'Via': '1.1 vegur'}
>>> r.status_code
200
>>> r.content
b'{\n  "id": 1,\n  "tipo": "pantalon",\n  "talle": 35\n}'
>>>