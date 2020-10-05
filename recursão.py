from toolz import cons, take, first


árvore = [1, [[2], 3], [4], 5, [6, 100, [[7], [[8]], 9]], 10]


def planificar(árvore):
    for ramo in árvore:
        if isinstance(ramo, list): yield from planificar(ramo)
        else: yield ramo


assert sum(planificar(árvore)) == 155


def somar_árvore(árvore):
    if len(árvore) == 0: return 0

    if isinstance(árvore[0], list):
        return somar_árvore(árvore[0]) + somar_árvore(árvore[1:])
    else:
        return árvore[0] + somar_árvore(árvore[1:])


assert somar_árvore(árvore) == 155


def profundidade(árvore):
    if isinstance(árvore, list):
        for ramo in árvore:
            yield from (1 + p for p in profundidade(ramo))
    else:
        yield 0


assert max(profundidade(árvore)) == 5


def count(i=1):
    while True:
        yield i
        i += 1


def sieve(numbers):
    p = next(numbers)
    yield from cons(p, sieve((n for n in numbers if n % p > 0)))


primes = sieve(count(2))
list(take(10, primes))
