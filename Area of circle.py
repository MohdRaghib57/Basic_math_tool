# area of a circle 

import math

r = float(input("Enter the radius of the circle: "))

#area = math.pi * r**2

area = math.pi * pow(r, 2)

area = round(area , 3)

print(f"the are of the circle is : {area} units^2")


