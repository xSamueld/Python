#Este ejercicio sirve para decir si el día que se pide es buen día o no.
n1 =str(input("ingrese un dia "))

day = ["lunes","Viernes","Sabado","Domingo"] 
n2 = day[0]
n3 = day[1]
n4 = day[2]
n5 = day[3]

if n1 == n2:
  print("Feliz lunes")

elif n1 == n3:
  print("Feliz Viernes")
  
elif n1 == n4:
  print("Feliz Sabado")

elif n1 == n5:
  print("Feliz Domingo")

else:
  print("mal dia xd")
