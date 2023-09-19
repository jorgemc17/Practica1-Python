""" Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después 
de cenar en un restaurante, generalmente una cantidad igual al 15% o más
del costo de su comida. Escriba un programa que pregunte al usuario 
cuánto fue su consumo en el restaurante y que porcentaje de propina desea 
dejar al mesero. Su programa debe devolver la cantidad de dinero a 
dejar como propina. """

consumo_usuario = float(input(" Digite cuanto fue su consumo: "))
porcentaje_propina = float(input("Digite cuanto porcentaje de propina desea dejar (unidades decimales): "))

if porcentaje_propina >=0.15 and porcentaje_propina < 1:
    print(f"La cantidad de propina a dejar es de: {porcentaje_propina*consumo_usuario}")
else:
    print("No admitido. El porcentaje minimo de propina es de 15% (=0.15)")
