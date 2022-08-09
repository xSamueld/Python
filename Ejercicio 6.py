#Dice en que equipo haz votado.
Partidos=("Rojo", "Verde", "Azul")
print(Partidos)

n1=str(input("elija un partido " ))

n2 = Partidos[0]
n3 = Partidos[1]
n4 = Partidos[2]

if n1 == n2:
  print("Usted ha votado por el equipo rojo :)")

elif n1 == n3:
  print("Usted ha votado por el equipo verde :)")

elif n1 == n4:
  print("Usted ha votado por el equipo Azul")
else:
  print("Opción errónea >:v")
