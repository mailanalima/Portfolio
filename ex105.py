def notas(* n):
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)

    return dados


resp = notas(5.5, 2.5, 8.5)
print(resp)
