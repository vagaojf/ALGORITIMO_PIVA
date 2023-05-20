idades = {
    "ana" : 34,
    "joao" : 54,
    "maria" : 19
}
maior = 0
maior_nome = ''

for nome in idades.keys():
    if len(nome) > maior:
        maior = len(nome)
        nome_maior = nome

print(f"o maior nome é {nome_maior} e sua idade é {idades.get(nome_maior)}")


