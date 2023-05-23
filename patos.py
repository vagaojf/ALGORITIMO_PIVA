def contar(cabecas, pes):
    coelhos = (pes - 2*cabecas)/2
    patos = (cabecas - coelhos)

    return coelhos, patos
print(contar(11, 34))


