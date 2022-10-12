# Reto8
def reto8():
  numero = int(input("Introduce un número: "))
  #Comprueba que se cumpla con cada número del rango si el resto de dividir da 0.
  for i in range(2,numero):
    if numero % i == 0:
      return print("No es primo")
  print ("Es primo")
      