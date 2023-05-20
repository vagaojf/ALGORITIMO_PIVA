def conveter(h, m, s):
    return (h * 3600 + m * 60 +s)

hora = input("digite a hora hh:mm:ss: ")
h = hora.split(":")
seg = segundos(int(h[0]), int(h[1], int(h[2]))