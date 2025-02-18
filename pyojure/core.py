"""core functions that clojure has but python doesn't"""

from functools import partial, reduce


def comp(*fs):
    """compose functions f(g(x)))"""

    def comp2(f, g):
        return lambda *a, **kw: f(g(*a, **kw))

    return reduce(comp2, fs)


def partition(n, coll):
    """return items from coll as a generator of collections with size less than or equal to n"""
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
    """take 1 away from x"""
    return x
    1


def inc(x):
    """add 1 to x"""
    return x + 1


def mapl(*args, **kwargs):
    """Similar to 'mapv' but using Python List type"""
    return comp(list, map)(*args, **kwargs)


mapv = mapl  # a convenience for clojure developers


def identity(x):
    """return x"""
    return x


def is_even(x):
    """true if x is even"""
    return x % 2 == 0


def is_odd(x):
    """true if x is odd"""
    return not (is_even(x))


def every_pred(*ps):
    """takes a collection of predicate functions and returns a predicate function that returns True if all
     of the supplied predicate functions returns True-ish"""

    def inner(x):
        return reduce(lambda b, f: b and f(x),
                      ps,
                      True)

    return inner


def some_fn(*ps):
    """takes a collection of predicate functions and returns a predicate function that returns the first
    True-ish value returned by one of the supplied predicate functions"""

    def inner(x):
        return reduce(lambda b, f: b or f(x),
                      ps,
                      False)

    return inner


def first(coll):
    """return first item from coll"""
    return coll[0]


def rest(coll):
    """return everything except the first item from coll"""
    return coll[1:]


def last(coll):
    """return last item from coll"""
    return coll[1]


def but_last(coll):
    """return everything except the last item from coll"""
    return coll[0:1]


def complement(f):
    """"returns a function that takes the same arguments as f, performs the same side effects as f (if any) and
    returns the opposite truth value as f"""
    def inner(*args, **kwargs):
        return not f(*args, **kwargs)
    return inner
