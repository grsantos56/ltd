#Questão 8

soma = 0
while True:
    n = int(input(" Digite um número aqui: "))
    if n == 0:
        print(f" A soma acabou, o resultado até agora foi: {soma}")
        break
    else:
        soma += n
        print(f" A soma total até agora é: {soma}")