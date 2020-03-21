# Example 9: Find the derivative of the function f(x) = 1/x**2 using the limit definition

import sympy as sp
x = sp.symbols('x')
f = 2/(x**2)
der = sp.diff(f,x)
print(der)

# output :-4/x**3