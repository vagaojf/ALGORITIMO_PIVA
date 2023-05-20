def anobi(x):
    if (x % 4 == 0):
        if (x % 100 == 0):
            if (x % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

x = int(input("digite o ano: "))
if anobi(x):
    print(f"{x} é um ano bissexto")
else:
    print(f"{x} é não é um ano bissexto")

