numbers = [1, 2, 3, 4, 5] # リストを定義
ans = 0 # 合計を保存する変数を0
for n in numbers: # リストnumbersの要素を1つずつ取り出して処理する
    if n % 2 == 0: # 偶数の値だけをansに足す
        ans += n
ans *= 2 # 合計した値を2倍する
print(ans) # 結果を表示
