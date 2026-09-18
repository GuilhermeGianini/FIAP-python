nums = []

for i in range(5):
    numero = int(input("Digite um número: "))
    nums.append(numero)

print("Lista completa:", nums)
print("Maior número:", max(nums))
print("Menor número:", min(nums))
print("Soma dos números:", sum(nums))