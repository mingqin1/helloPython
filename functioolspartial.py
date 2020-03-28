from operator import mul
from functools import partial
"""Create new triple function from mul, binding first positional argument to 3
mul (a, b)  = mul(3, b)
"""
triple = partial(mul, 3)

"""triple(7) =  mul (3,7)
"""
print(triple(7))
