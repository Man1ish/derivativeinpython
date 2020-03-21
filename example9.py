# Example 9: Find the derivative of the function f(x) = 1/(x-1) using the limit definition

import sympy as sp
x = sp.symbols('x')
f = 1/(x-1)
der = sp.diff(f,x)
print(der)

# output :-1/(x-1)**2