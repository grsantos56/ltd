listaNumeros = []
mediaNumeros = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    listaNumeros.append(numero)
    mediaNumeros += numero
mediaNumeros /= len(listaNumeros)
print(f"A média dos números digitados é: {mediaNumeros}")