"""core functions that clojure has but python doesn't"""

from functools import partial, reduce


def comp(*fs):
    """compose functions f(g(x)))"""
    def comp2(f, g):
        return lambda *a, **kw: f(g(*a, **kw))

    return reduce(comp2, fs)


def partition(n, coll):
    for i in range(0, len(coll), n):
        yield coll[i: i + n]


def concat(*xs):
    """concatenate collections into one collection"""
    return reduce(list.__add__, xs)


def assoc(d, *kvs):
    """produce a copy of d with kvs in it"""
    def assoc1(m, k, v):
        n = m.copy()
        n[k] = v
        return n

    return reduce(lambda m, kv: assoc1(m, kv[0], kv[1]), partition(2, kvs), d)


def dissoc(d, *ks):
    """produce a copy of d without ks in it"""
    def dissoc1(m, k):
        n = m.copy()
        n.pop(k)
        return n
    return reduce(lambda m, k: dissoc1(m, k), ks, d)


def dec(x):
    return x - 1


def inc(x):
    return x + 1


def mapl(*args, **kwargs):
    """Similar to 'mapv' but using Python List type"""
    return comp(list, map)(*args, **kwargs)


mapv = mapl  # a convenience for clojure developers


def identity(x):
    return x


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return not(is_even(x))


def every_pred(*ps):
    """return True if EVERY PREDICATE FUNCTION returns True-ish"""
    def inner(x):
        return reduce(lambda b, f: b and f(x),
                      ps,
                      True)
    return inner
