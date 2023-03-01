# Reto16
def reto16():
  from calendar import datetime
  fecha1 = datetime.date(2022,8,31)
  fecha2 = datetime.date(2022,9,20)
  dif_fecha = fecha2-fecha1
  print (f'La diferencia entre la fecha {fecha1} y la fecha {fecha2} es de {dif_fecha.days} días.')
  