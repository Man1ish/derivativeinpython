# Example 6: Using the definition of the derivative, differentiate the function

import sympy as sp
x = sp.symbols('x')
f =  x ** 2 + 2*x - 2
der = sp.diff(f,x)
print(der)

# output :2x+2