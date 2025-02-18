# pyojure

make python more like clojure

![pyojure is pure joy](6vc5do.jpeg "python doesn't have to be so hard")

## Usage

```pycon
>>> from pyojure import *
>>> mapv(print, dir())
```

```pycon
>>> assoc({"this": "is"}, "very", "cool")
{'this': 'is', 'very': 'cool'}
>>> comp(str, inc, int)('123')
'124'
>>> list(partition(2, [1,2,3,4,5,6,7,8,9]))
[[1, 2], [3, 4], [5, 6], [7, 8], [9]]
```

### Doc

```pycon
>>> import pyojure
>>> help(pyojure.core)
```

## Caveats
* Clojure has much more liberal syntax for identifiers.  Standard naming transpositions are attempted.
  * `-` -> `_` e.g. `every-pred` -> `every_pred`
  * `?` predicate suffix -> `is_`/`has_`/etc. predicate prefix e.g., `odd?` -> `is_odd`
* Some Clojure function names indicate types that are known by different names in Python.
  * E.g., the `v` in `mapv` refers to the Clojure `vector` type, which is equivalent to a Python `list`
  * Both names are provided _for now_ i.e., `mapv` == `mapl`
