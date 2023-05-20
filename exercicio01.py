def epar(x):
    return (x % 2 == 0)
    pass

n = int(input("digite um numero: "))
if epar(n):
    print("o numero é par!")
else:
    print("o numero é impar!")
