import math
from math import sin

h = (math.pi/2)/100
integral = 0.5 * (sin(0)+sin(math.pi/2))

for i in range(1 ,100):
    integral += sin(i*h)
integral *= h

print(integral)