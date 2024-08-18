a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
if a <= 1:
    print("素数ではありません")
else:
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            print("素数ではありません")
            break
        else:
            print("素数です")