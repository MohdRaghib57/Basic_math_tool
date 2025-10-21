# hypoteneus or right triangle (L4 ex3)

import math

a = float(input("Enter length of base: "))
b = float(input("Enter length of height: "))

#c = math.sqrt(a**2 + b**2)

c = math.sqrt(pow(a,2) + pow(b,2))

c = round(c,2)

print(f"The length of the hypotenuse is: {c} units")

