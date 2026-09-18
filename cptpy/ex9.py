negativos = []
positivos = []
numeros = []
while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break

    numeros.append(numero)

for numero in numeros:
    if numero > 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

print("Números positivos:", positivos)
print("Números negativos:", negativos)