palindromo = str(input("ingrese palindromo ")) 
#se le pide a la persona que ingrese un palindromo

revisar = palindromo[::-1] 
#Aqui se utiliza revisar como una variable, para que así [::-1] le pueda dar vuelta a la palabra y así comprobar si es palindromo o no.

espacio = revisar.replace(" ","") 
#Aqui utilizo espacio como una variabke para poder quitar los espacios de la palabra revisada, en este caso el replace quita los espacios del palindromo.
print(espacio)
