n1 = int(input("ingrese un numero "))# se le pide a la persona que ingrese dos numeros

n2 = int(input("ingrese un numero "))

respuesta = n1**(1/n2) #Ya que no se puede utilizar la raiz en python, se utiliza su operacion contraria la cual es la potencia, como debemos de elevar el primer numero con el segundo, tomamos el segundo numero y lo ponemos en una fracción para así poder operarlo.

print(respuesta)
