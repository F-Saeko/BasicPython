import math
from math import sin

def trapezoidal_integral(f, a, b ,n):

    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1 ,n):
        integral += f(a + i * h)
    integral *= h

    return  integral

# (1)
result1 = trapezoidal_integral(lambda x: sin(x), 0, math.pi/2, 50)
print(result1)

# (2)
result2 = trapezoidal_integral(lambda x: 4/(1+x**2), 0, 1, 100)
print(result2)

# (3)
result3 = trapezoidal_integral(lambda x: math.sqrt(math.pi) * math.exp(-x ** 2), -100, 100, 1000)
print(result3)