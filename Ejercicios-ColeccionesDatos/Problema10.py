""" Problema 10:
Escriba un programa para imprimir una lista específica después de 
eliminar los elementos que se encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']
 """

lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
lista_muestra.remove(lista_muestra[0])
lista_muestra.remove(lista_muestra[4])
lista_muestra.remove(lista_muestra[3])

print(lista_muestra)