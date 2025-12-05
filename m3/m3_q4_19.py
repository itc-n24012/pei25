list_a = [] # list_aを作成
for x in range(1, 10): # 1から9までの整数をループさせる
    if x % 2 == 1: # 2で割った余りが1
        continue
    list_a.append(x) # xが偶数の場合、list_aの末尾にxを追加する
print(list_a) # list_aを出力
