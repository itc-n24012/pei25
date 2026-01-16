name_a = 'ant' # 文字列'ant'を変数name_aに代入
name_b = 'Attention please' # 別の文字列を変数name_bに代入
strs = '' # 空の文字列
for b in name_b: # name_bを1文字ずつ取り出して繰り返す
    if name_a.find(b) >= 0: # find()は見つかれば0以上、見つからなければ-1を返す
        strs += b # strsの末尾に追加する
print(strs) # 結果を表示
