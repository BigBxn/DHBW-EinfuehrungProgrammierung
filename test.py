import sympy as sp

A=sp.Matrix([[5,3,-2],[2,-7,4],[5,6,6]])
b=sp.Matrix([3,6,11])
x=A.LUsolve(b)
x, sum(x)
print(sum(x))