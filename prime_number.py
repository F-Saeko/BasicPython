def prime_number(n):
    if n <= 0:
        raise ValueError("エラー: 自然数ではありません")
    elif n == 1:
        raise ValueError("エラー: 1より大きい自然数を入力してください")

    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
   
while True:
    try:
        n = float(input("1より大きい自然数を入力してください: "))
        if not n.is_integer():
            raise ValueError("エラー: 自然数ではありません")
    
        n = int(n)
        result = prime_number(n)
        if result:
            print(f"{n}は素数です")
        else:
            print(f"{n}は素数ではありません")
        break

    except (ValueError, TypeError) as e:
        print(e)
        print("もう一度入力してください")