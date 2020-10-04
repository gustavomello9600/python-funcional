head = lambda s: s[0]
tail = lambda s: s[1:]

árvore = [1, [[2], 3], [4], 5, [6, 100, [[7], [[8]], 9]], 10]


def planificar(árvore):
    for ramo in árvore:
        if isinstance(ramo, list):
            yield from planificar(ramo)
        else:
            yield ramo

            
assert sum(planificar(árvore)) == 155


def somar_árvore(L):
    if L: head(L)
    else: return 0
    
    if isinstance(head(L), list):
        return somar_árvore(head(L)) + somar_árvore(tail(L))
    else:
        return head(L) + somar_árvore(tail(L))

    
assert somar_árvore(árvore) == 155


def profundidade(árvore):
    if isinstance(árvore, list):
        for ramo in árvore:
            yield from (1 + p for p in profundidade(ramo))
    else:
        yield 0


assert max(profundidade(árvore)) == 5
