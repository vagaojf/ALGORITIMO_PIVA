def eprimo(n):
    i = 1
    contador = 0
    while i <= n:
        if (n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False

x = int(input("digite um numero: "))
if eprimo(x):
    print(f"o numero {x} é primo!")
else:
    print(f"o numero {x} não é primo")



