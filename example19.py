# Example 18: Find the derivative of the power function  f(x) = x**n

import sympy as sp
x,n = sp.symbols('x,n')
f = x**n
der = sp.diff(f,x)
print(der)

# output : n*x**n/x