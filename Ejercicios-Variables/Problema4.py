""" Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el 
usuario y después muestre en pantalla la suma de todos los enteros desde 
1 hasta N. La suma de los N primeros enteros positivos puede ser calculada
de la siguiente forma: """

N = int(input("Digite un entero positivo: "))
if N >=1:
    suma = (N*(N+1))/2
    print(f" LA suma de los N primeros enteros positivos es de: {int(suma)} ")
else:
    print(" No digito correctamente el entero positivo")