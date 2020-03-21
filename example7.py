# Example 7: Determine the derivative of a quadratic function of general form

import sympy as sp
x,a,b,c = sp.symbols('x,a,b,c')
f = a*x**2 +b*x+c
der = sp.diff(f,x)
print(der)

# output :2ax+b