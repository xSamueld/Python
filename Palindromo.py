#Este programa identifica si una palabra el palindromo o no.
palindromo = str(input("ingrese palindromo ")) 

revisar = palindromo[::-1] 

espacio = revisar.replace(" ","") 
print(espacio)
