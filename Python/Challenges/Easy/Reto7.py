# Reto7
def reto7():
  password = "joel245"
  input_password = input("Introduce la contraseña: ")
  #Creamos nueva variable en minúsculas para no modificar la original.
  input_pass = input_password.lower()
  if (input_pass == password):
    print(f'¡Contraseña correcta!')
  else:
    print(f'Lo siento, la contraseña no coincide.')