# En esta variable pedimos una palabra
x=str(input("Ingrese una palabra:"))
#Aquí vamos a buscar la inicial de la palabra
y= x[0]
# Aqui utilizamos un if en donde ponemos todas las vocales para si comienza con vocales imprimir "inicia con vocales."
if y =="a" or y == "e" or y == "i" or y == "o" or y == "u" or y == "A" or y == "E" or y =="I" or y == "O" or y == "U": 
  print("Inicia con vocales")
  #Este else sirve para que cuando la palabra que se ingrese no comience con vocal aparezca que inicia con consonante.
else:
   print("Inicia con consonantes")
