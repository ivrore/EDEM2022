# Reto17
def reto17():
  tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# Encontrar los elementos de 3 a 5
  print(f'Estos son los elementos de 3 a 5: {tupla[2:5]}')
# Encontrar los 6 primeros elementos
  print(f'Estos son los 6 primeros elementos: {tupla[:6]}')
# Muestra la tupla desde el 5 elemento hasta el final
  print(f'Estos son los elementos desde el quinto hasta el final: {tupla[4:]}')
# Muestra toda la tupla haciendo uso de [:]
  print(f'Esta es la tupla entera: {tupla[:]}')
# Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
  print(f'Desde la posición dos a la nueve de dos en dos: {tupla[1:9:2]}')
# Devuelve la tupla con un salto cada 4 elementos
  print(f'Esta es la tupla cada 4 elementos: {tupla[: :4]}')
# Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
  print(f'Muestra desde la posición 9 a la 2: {tupla[-2:-10:-1]}')
  
  