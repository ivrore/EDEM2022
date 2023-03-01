# Reto14
def reto14():
  import math
  r = float(input("Introduce el radio del círculo: "))
  area_circulo = ((float(math.pi)*r)**2)
  def volumen_cilindro(l):
    return area_circulo*l
  l = float(input("Introduce la longitud del círculo: "))
  print(f'El volumen del cilindro es {round(volumen_cilindro(l),2)} cm2')