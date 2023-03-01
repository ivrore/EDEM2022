# Reto5
def reto5():
  #Definimos las variables
  password_correcta:str ="admin"
  password:str = input("Introduce la contraseña: ")
  #No sale del bucle hasta que hacierte la contraseña
  while (password != password_correcta ) :
   password = input ("Introduce la contraseña de nuevo: ")
  print('Bienvenido al programa señor ADMIN')
