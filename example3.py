# Using the limit definition find the derivative of the function f(x) = 3x + 2

import sympy as sp
x = sp.symbols('x')
f = 3* x + 2
der = sp.diff(f,x)
print(der)

# output : 3