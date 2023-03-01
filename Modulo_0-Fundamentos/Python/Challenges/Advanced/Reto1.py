def Reto1():
  disco1 = {"Nombre":"Help!","Artista":"The Beatles","Año":1965,"Precio":14.99,"Género":"Pop"}
  disco2 = {"Nombre":"The North Water","Artista":"Tim Hecker","Año":2018,"Precio":12.99,"Género":"Electro"}
  disco3 = {"Nombre":"Leggendaddy","Artista":"Daddy Yankee","Año":2022,"Precio":16.99,"Género":"Reggaeton"}
  disco4 = {"Nombre":"Live in Texas","Artista":"Linkin Park","Año":2003,"Precio":13.99,"Género":"Rock"}
  disco5 = {"Nombre":"Du hast","Artista":"Ramstein","Año":1997,"Precio":14.99,"Género":"Metal"}
  disco6 = {"Nombre":"Focus","Artista":"Cynic","Año":1993,"Precio":11.99,"Género":"Death Metal"}
  disco7 = {"Nombre":"Filosofem","Artista":"Burzum","Año":1993,"Precio":16.99,"Género":"Black Metal"}
  lista_discos = [disco1,disco2,disco3,disco4,disco5,disco6,disco7]
  print("''''''''''''''''''''''''''''''''''''")
  print('¡Bienvenido a la tienda TotalMusic!')
  print("''''''''''''''''''''''''''''''''''''")
  print("\nA continuación te mostramos los discos que tenemos actualmente disponibles: \n")  
  for disco in lista_discos:
    print(str(lista_discos.index(disco)+1)+"."+disco["Nombre"]+" ("+disco["Artista"]+")")
  
  disco_elegido = int(input("\nElige el disco que deseas comprar: "))
  if disco_elegido == 0:
    print("¡Gracias por tu visita!, a la próxima habrá más suerte")
  elif disco_elegido != 0:
    disco_comprado = lista_discos[disco_elegido-1]
    if disco_comprado["Género"] == "Black Metal"or disco_comprado["Género"] =="Electro":
      print(f'\n¡Estás de suerte! El disco que has comprado es {disco_comprado["Nombre"]} de {disco_comprado["Artista"]} y está en oferta con un 30% de dto. Por lo tanto, de un precio inicial de {disco_comprado["Precio"]}€ el precio final se queda en {round(disco_comprado["Precio"]*0.7,2)}€\n')
      terminar = input("Pulsa 0 para terminar tu compra: ")
      while terminar != "0":
        terminar = input("Pulsa 0 para terminar tu compra: ")
      print("¡Muchas gracias, hasta la próxima!")
    else:
      print(f'\nEl disco que has elegido es {disco_comprado["Nombre"]} de {disco_comprado["Artista"]} y tiene un precio de {disco_comprado["Precio"]}€\n\n')
      terminar = input("Pulsa 0 para terminar tu compra: ")
      while terminar != "0":
        terminar = input("Pulsa 0 para terminar tu compra: ")
      print("¡Muchas gracias, hasta la próxima!")
  return 