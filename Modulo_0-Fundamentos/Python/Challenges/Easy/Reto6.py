# Reto6
def reto6():
  user_age = int(input("Introduce tu edad: "))
  while (user_age <= 0 or user_age >= 109):
    user_age = int(input("Introduce tu edad correcta: "))
  if (user_age >= 18):
    print(f'¡Genial! Tienes {user_age} años, por lo tanto eres mayor de edad.')
  elif (user_age <18):
    print(f'¡Lo siento! Tienes {user_age} años, por lo tanto eres menor de edad.')
