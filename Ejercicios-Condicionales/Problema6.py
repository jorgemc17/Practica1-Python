""" Problema 6:
Escribir un programa para una empresa que tiene salas de juegos para 
todas las edades y quiere calcular de forma automática el precio que debe 
cobrar a sus clientes por entrar. El programa debe preguntar al usuario la 
edad del cliente y mostrar el precio de la entrada. Si el cliente es menor 
de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 
y si es mayor de 18 años, S10. """

edad_cliente = int(input("Digite su edad: "))
if edad_cliente < 4 and edad_cliente >0:
    print(f"Con {edad_cliente} usted entra GRATIS")
elif edad_cliente >=4 and edad_cliente <=18:
    print(f"Con {edad_cliente} usted debe pagar $5")
elif edad_cliente >18:
    print(f"Con {edad_cliente} usted debe pagar $10")
else:
    print("Ha digitado mal su edad")