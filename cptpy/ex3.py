notas = []

notas.append(float(input("digite a primeira nota: ")))
notas.append(float(input("digite a segunda nota: ")))
notas.append(float(input("digite a terceira nota: ")))

media = sum(notas) / 3

print("A média é:", media)

if media >= 7:
    print("aprovado")
else:
    print("reprovado")