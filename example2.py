# Calculate the derivative of the function y = x.
import sympy as sp
x = sp.symbols('x')
f = x
der = sp.diff(f,x)
print(der)

# Output = 1