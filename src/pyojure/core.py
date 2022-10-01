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


def assoc(d, *ts):
    """produce a copy of d with ts in it"""
    def assoc1(m, k, v):
        n = m.copy()
        n[k] = v
        return n

    return functools.reduce(lambda m, t: assoc1(m, t[0], t[1]), partition(2, ts), d)
