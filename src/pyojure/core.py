"""core functions that clojure has but python doesn't"""

import functools


def comp(*fs):
    """compose functions f(g(x)))"""
    def comp2(f, g):
        return lambda *a, **kw: f(g(*a, **kw))

    return functools.reduce(comp2, fs)


def partition(n, coll):
    for i in range(0, len(coll), n):
        yield coll[i: i + n]


def assoc(d, *kvs):
    """produce a copy of d with ts in it"""
    def assoc1(m, k, v):
        n = m.copy()
        n[k] = v
        return n

    return functools.reduce(lambda m, kv: assoc1(m, kv[0], kv[1]), partition(2, kvs), d)


def dissoc(d, *ks):
    """produce a copy of d without ts in it"""
    def dissoc1(m, k):
        n = m.copy()
        n.pop(k)
        return n
    return functools.reduce(lambda m, k: dissoc1(m, k), ks, d)


def dec(x):
    return x - 1


def inc(x):
    return x + 1


