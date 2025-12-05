list_a = [] # list_aを作成
for x in range(1, 30): # 1から30までの整数をループさせる
    if x % 2 == 0: # 2で割った余りが0
        continue
    list_a.append(x) # xが奇数の場合、list_aの末尾にxを追加する
print(list_a) # list_aを出力
