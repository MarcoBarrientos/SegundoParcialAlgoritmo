def calcular_promedio(valor1, valor2, valor3):
    suma = valor1 + valor2 + valor3
    promedio = suma / 3
    return promedio

valor1 = int(input("Ingrese el primer entero: "))
valor2 = int(input("Ingrese el segundo entero: "))
valor3 = int(input("Ingrese el tercer entero: "))

promedio = calcular_promedio(valor1, valor2, valor3)
print("El valor promedio es:", promedio)
