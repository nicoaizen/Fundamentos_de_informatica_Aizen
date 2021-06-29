r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
r.json()
>>> r.headers  
{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '0', 'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"', 'Vary': 'Accept-Encoding', 'Date': 'Thu, 
06 May 2021 14:20:04 GMT', 'Via': '1.1 vegur'}
>>> r.status_code
404