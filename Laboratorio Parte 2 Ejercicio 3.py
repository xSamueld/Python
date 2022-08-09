nombre1 = str(input("Ingrese su nombre: ")) #Se debe de pedir los dos nombres y el primer apellido.
nombre2 = str(input("Ingrese su segundo nombre: "))
apellido = str(input("Ingrese sus apellidos: "))
x = nombre2.replace(" ","") # x nos sirve para poder eliminar los espacios que sobram ya que el correo debe de ir junto.

y = nombre1[0]+nombre1[1] # y sirve para poder extraer las primeras dos letras del primer nombre.

print(y+"."+x+"@baco.com") #Este print lo que hace es juntar y, ., x y baco para así crear un correo.
