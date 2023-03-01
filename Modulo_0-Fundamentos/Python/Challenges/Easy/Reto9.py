# Reto9
def reto9():
  year = int(input("Introduce un año para comprobar si es bisiesto: "))
  if (year % 4 == 0 or (year % 100 != 0 and year % 400 == 0 )):
    print(f'El año {year} es bisiesto')
  else:
    print(f'El año {year} no es bisiesto')

      