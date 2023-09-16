def calcular_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

lado1_rectangulo1 = float(input("Ingrese el primer lado del rectángulo 1: "))
lado2_rectangulo1 = float(input("Ingrese el segundo lado del rectángulo 1: "))

lado1_rectangulo2 = float(input("Ingrese el primer lado del rectángulo 2: "))
lado2_rectangulo2 = float(input("Ingrese el segundo lado del rectángulo 2: "))

superficie_rectangulo1 = calcular_superficie(lado1_rectangulo1, lado2_rectangulo1)
superficie_rectangulo2 = calcular_superficie(lado1_rectangulo2, lado2_rectangulo2)

if superficie_rectangulo1 > superficie_rectangulo2:
    print("El rectángulo 1 tiene una superficie mayor.")
elif superficie_rectangulo2 > superficie_rectangulo1:
    print("El rectángulo 2 tiene una superficie mayor.")
else:
    print("Ambos rectángulos tienen la misma superficie.")
