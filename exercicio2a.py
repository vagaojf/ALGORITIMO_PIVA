dic = {}
for i in range(5):
    nome = str(input(f"digite o {i+1}o nome! "))
    idade = int(input(f"digite a {i+1}a idade! "))
    dic[nome] = idade
soma = 0
for idade in dic.values():
    soma += idade
media = soma / len(dic)
print(f"a media das idades é {media}")

for nome, idade in dic.items():
    if idade > media:
        print(f"{nome} tem {idade} anos!")
