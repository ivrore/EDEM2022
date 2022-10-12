# Reto13
def reto13():
#Definimos la función que realiza el cálculo del area 
  def area_triangulo(a :float,b: float):
    return (a * b) / 2
#Pedimos al usuario que introduzca las la altura y la base con decimales
  a = float(input("Introduce la altura en cm: "))
  b = float(input("Introduce la longitud de la base del tríangulo en cm: "))

  print (f'El area del triángulo es {area_triangulo(a,b)} cm2')