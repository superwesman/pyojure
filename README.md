# pyojure

make python more like clojure

![pyojure is pure joy](6vc5do.jpeg "python doesn't have to be so hard")

## Usage

```python
from pyojure import *

>>> assoc({"this": "is"}, "very", "cool")
{'this': 'is', 'very': 'cool'}
>>> comp(str, inc, int)('123')
'124'
>>> list(partition(2, [1,2,3,4,5,6,7,8,9]))
[[1, 2], [3, 4], [5, 6], [7, 8], [9]]

```