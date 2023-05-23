def primo(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
        else:
            return True
    elif number == 0:
        return False
    elif number == 1:
        return False
    else:
        return False

def lista(num):
    primos = []
    cont = 2
    while len(primos) < num:
        if primo(cont):
            primos.append(cont)
        cont += 1
    return primos
def somalista(number):
    soma = 0
    for i in number:
        soma += i
    return soma

valor = int(input("digite os dois ultimos numeros do RA: "))
print(somalista(primo(valor * 2 + 5)))