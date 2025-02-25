def euclid(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

#(3-1)
result1 = euclid(10, 20)
print(result1)

#(3-2)
result2 = euclid(14, 91)
print(result2)

#(3-3)
result3 = euclid(91, 14)
print(result3)


#問4
def Coprime(a,b):
   result = euclid(a,b)
   if result == 1:
       print("互いに素")
   else:
       print("互いに素ではない")

#(4-1)
Coprime(10,20)

#(4-2)
Coprime(14,91)

#(4-3)
Coprime(91,14)
