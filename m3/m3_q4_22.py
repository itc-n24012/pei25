a = [1, 2, 3] # リストaを定義
b = [1, 2, 3] # リストbを定義
c = a + b

if a is b: # False 
    print(1)
elif a + b is c: # False
    print(2)
elif a == b: # Ture
    print(3)
elif a + b == c: # プログラムが終了
    print(4)
