def euclid(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

#(1)
result1 = euclid(10, 20)
print(result1)

#(2)
result2 = euclid(14, 91)
print(result2)

#(3)
result3 = euclid(91, 14)
print(result3)