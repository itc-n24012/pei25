a = 10 # 変数aに10を代入
b = 1 # 変数bに1を代入
x = [] # 変数xに空のリストを代入

while b <= 3: # whileループ
    y = divmod(a, b)
    y = list(y)
    x += y
    b += 1

x = tuple(x) # リストxをタブルに変換し、xに再代入
print(x)
