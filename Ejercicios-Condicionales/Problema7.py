""" Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir 
entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de
 que no es correcta. """

primer_numero = float(input("Digite el primer numero: "))
segundo_numero = float(input("Digite el segundo numero: "))
opcion_elegida = int(input("\n \t Menu \n 1)Mostrar una suma de los dos números \n 2)Mostrar una resta de los dos números \n 3)Mostrar una multiplicación de los dos números \n Opcion: "))

if opcion_elegida == 1:
    print(f" La suma de ambos numeros es {primer_numero + segundo_numero}")
elif opcion_elegida == 2:
    print(f" La resta de ambos numeros es {primer_numero - segundo_numero}")
elif opcion_elegida == 3:
    print(f" La multiplicacion de ambos numeros es {primer_numero * segundo_numero}")
else:
    print(f"Tu opcion {opcion_elegida} es invalida/incorrecta")