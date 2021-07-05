# Para pensar 🤔: Dado el siguiente texto:
# texto = 'Esta es la linea uno\npalabra en la linea dos\n'
# ¿Cómo crees que darán las siguientes búsquedas?
# expresion regular a: '^palabra'
# 	Podría devolver la cantidad de veces que aparece en el texto "palabra" al principio de una línea o dónde está o un booleano que confirme que lo encontró.  
# expresion regular b: '\Apalabra'
# 	Se fija si al comienzo del texto está "palabra" y podría devolver un booleano.
# expresion regular c: 'palabra$'
# 	Podría devolver la cantidad de veces que aparece en el texto "palabra" al final de una línea o dónde está o un booleano que confirme que lo encontró.
# expresion regular d: 'palabra\Z'
# 	Podría devolver la cantidad de veces que aparece en el texto "palabra" al principio de una línea o dónde está o un booleano que confirme que lo encontró.
# Para pensar 🤔: ¿Qué significará la expresión regular "X(.*)Y"? 
# Ennumera algunas de las posibles strings que cumplen con dicha condición.
# 	Significa todos los caracteres que se encuentren entre X e Y. 
# 	Las secuencias de escape son una combinación de caracteres que tiene un significado distinto de los caracteres literales 
# 	contenidos en ella y se utilizan para definir ciertos caracteres especiales dentro de cadenas de teX(to, 
# 	tipicamente aquellos que dan formato al mismo. )Y aún cuando son un conjunto de caracteres, una secuencia de escape se considerada un carácter único.
# Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
# 	\d{4,}
# Desafío II: ¿Construí la expresión regular que obtenga al menos entre 3 y 6 letras minúsculas?
# 	[a-z]{3,6}
# Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
# 	ab*
# Para pensar 🤔: ¿Existe una única respuesta para los ejercicios? ¿Qué otras alternativas se te ocurren?
# 	Más debe haber, que las sepamos es otra cosa.
# Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
# texto = 'En la clase de Introducción a la programación hay 30 estudiantes'
# 	\d
# Para pensar 🤔: ¿Qué resultado obtenemos al ejecutar en la última linea?
# 	true o la posición de los caracteres
# Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 ¿Qué resultado obtenés? ¿Qué quiere decir el mensaje span?
# 	<re.Match object; span=(22, 26), match='amet'>
# Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función match()?
# 	Nulo. Devuelve solo lo que esta al comienzo.
# Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función group()?
# 	Devuleve "amet". Agrupa los caracteres que encontró y los devuelve como string.
# Para pensar 🤔: ¿Qué resultado obtenemos?
# 	Findall busca todas las coincidencias del patrón y devuelve una lista
# Desafio VI: Expresá el patron de búsqueda utilizando lo visto anteriormente sobre metacaracteres y rangos.
# Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función sub?
# 	Para reemplazar todas las ocurrencias del patrón por otro patrón.