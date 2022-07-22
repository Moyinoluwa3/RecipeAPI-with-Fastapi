import numpy as np
print("WELCOME TO A QUADRATIC EQUATION PROGRAM")

a = int(input("What is the coefficient of X: "))
b = int(input("What is the coefficient of Y: "))
c = int(input("What is the coefficient of X: "))
coeff = [a,b,c]
answer = np.roots(coeff)
print("The roots of the equation are", answer)


