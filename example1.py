# Using the definition of derivative, prove that the derivative of a constant is
#Import sympy library
import sympy as sp
x = sp.symbols('x')
f =100
der = sp.diff(f,x)
print(der)

#Output: 0