def somadigitos(number):
    soma = 0
    for x in number:
        soma += int(x)
    return soma

def multdigitos(number):
    multipl = 1
    for x in number:
        multipl *= int(x)
    return multipl

ra = input("Digite um número positivo: ")

# Verificar se o número é positivo
if int(ra) > 0:
    soma = somadigitos(ra)
    multiplicacao = multdigitos(ra)
    print("Soma dos dígitos:", soma)
    print("Multiplicação dos dígitos:", multiplicacao)
else:
    print("Número inválido. Digite um número positivo.")