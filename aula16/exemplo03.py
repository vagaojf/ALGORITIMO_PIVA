def retorna_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dicio = {"nome": "vagner"}
print(retorna_valor(dicio, 5))