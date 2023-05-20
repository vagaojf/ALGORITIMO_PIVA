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

print("os 50 primeiros numeros primos são: ")
i, n = 2, 0
while n <= 50:
    if eprimo(i):
        print(i, end=" - ")
        n += 1
    i += 1