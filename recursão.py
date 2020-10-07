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


###################
# Torres de Hanoi #
###################
from functools import partial
from typing import List, Tuple

from toolz import nth, cons

Stack = List[int]
Context = Tuple[Stack, Stack, Stack]

index_to_name = ("A", "B", "C")


def where(n: int, context: Context) -> int:
    return nth(0,
               nth(0,
                   filter(lambda result: result[1],
                          list(enumerate(
                          map(lambda stack: n in stack,
                              context))))))


def move(n: int, target_stack_index: int, context: Context, logs: List[str]
        ) -> Tuple[Context, List[str]]:
    current_stack_index = where(n, context)
    current_stack = nth(current_stack_index, context)
    target_stack = nth(target_stack_index, context)
    untouched_stack_index = nth(0, set(range(3))
                                   - {target_stack_index,
                                      current_stack_index})
    untouched_stack = nth(untouched_stack_index, context)

    if n == min(current_stack):
        if len(target_stack) == 0 or n < min(target_stack):
            _, *new_current_stack = current_stack
            new_target_stack = list(cons(n, target_stack))

            new_context = tuple(
                map(lambda tup: nth(1, tup),
                sorted(((target_stack_index, new_target_stack),
                        (current_stack_index, new_current_stack),
                        (untouched_stack_index, untouched_stack))))
            )

            log = (f"{index_to_name[current_stack_index]}"
                   + f" to {index_to_name[target_stack_index]}")
            new_logs = logs + [log]

            return new_context, new_logs
        else:
            new_context, new_logs = move(min(target_stack),
                                         untouched_stack_index,
                                         context,
                                         logs)
            return move(n, target_stack_index, new_context, new_logs)
    else:
        new_context, new_logs = move(min(current_stack),
                                     untouched_stack_index,
                                     context,
                                     logs)
        return move(n, target_stack_index, new_context, new_logs)


move6 = partial(move, 6, 2)
move5 = partial(move, 5, 2)
move4 = partial(move, 4, 2)
move3 = partial(move, 3, 2)
move2 = partial(move, 2, 2)
move1 = partial(move, 1, 2)

context, logs = move1(
                *move2(
                *move3(
                *move4(
                *move5(
                *move6(([1, 2, 3, 4, 5, 6], [], []), [])
                )))))
print(f">> Solved:\n{context}")
print("\n")
print(f"> steps:")
for i, step in enumerate(logs):
    print(f"{i + 1}. {step}")
