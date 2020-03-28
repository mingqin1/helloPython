
from copy import deepcopy
a = [10, 20]
b = [a, 30]
a.append(b)


c = deepcopy(a)

