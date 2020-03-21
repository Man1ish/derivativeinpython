# Example 5: Using the definition, find the derivative of the simplest quadratic function

import sympy as sp
x = sp.symbols('x')
f =  x ** 2
der = sp.diff(f,x)
print(der)

# output :2x