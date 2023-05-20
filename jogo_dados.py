from roladado import dados

while True:
    entrada = input("precione enter para jogar")
    usuario = dados()
    print("agora é minha vez de jogar...")
    for i in range(1, 1000):
        pass
    computador = dados()
    print(f"voce {usuario} - Eu {computador}")
    if usuario > computador:
        print("voce ganhou :)")
    elif computador == usuario:
        print("empatamos")
    else:
        print("eu ganhei")
        entrada = input("deseja continuar S ou N ?").upper()
    if entrada == N
        break
