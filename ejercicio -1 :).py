#Este progrmaa pide un numero e identifica si es primos y los divisores.
n=int(input("Ingrese un numero "))

contador=1
divisores=0

while contador<=n:
  residuo=n%contador
  print(residuo)
  if residuo == 0:
    divisores=divisores+1
  contador=contador+1
if divisores==1:
  print ("no es primo")
  print("Tiene ",divisores, " divisores")
else:
  print("es primo")
  print("Tiene ",divisores, " divisores")
