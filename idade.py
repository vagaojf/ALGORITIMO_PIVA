idades = {
    "ana" : 34,
    "joao" : 54,
    "maria" : 19
}
soma = 0
for idade in idades.values():
    print("a idade que esta sendo somada agora é", idade)
    soma += idade

media = soma / len(idades)

print(f"a media das idades é {media}")

