a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
b = int(b)

if a <= 1:
    print(str(a) + "は素数ではありません")
else:
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            print(str(a) + "は素数ではありません")
            break
    else:
        print(str(a) + "は素数です")

if b <= 1:
    print(str(b) + "は素数ではありません")
else:
    for i in range(2, int(b**0.5)+1):
        if b % i == 0:
            print(str(b) + "は素数ではありません")
            break
    else:
        print(str(b) + "は素数です")
        