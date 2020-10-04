árvore = [1, [[2], 3], [4], 5, [6, 100, [[7], [[8]], 9]], 10]

def planificar(árvore):
    for ramo in árvore:
        if isinstance(ramo, list):
            yield from planificar(ramo)
        else:
            yield ramo

sum(planificar(árvore))


def somar_árvore(L):
    if L: head = L[0]
    else: return 0
    
    if isinstance(head, list):
        return somar_árvore(head) + somar_árvore(L[1:])
    else:
        return head + somar_árvore(L[1:])

somar_árvore(árvore)
