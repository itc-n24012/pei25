a = 0 # 変数aを0
counter = 0 # counter用の変数を0
while counter < 6: # counterが6未満の間、繰り返し処理を行う
    a += counter # aにcounterの値を加える
    counter += 1 # counterを1増やす
    if a > 4: # aが4より大きくなったら
        break # whileループを終了する
print(a, counter) # aとcounterの値を表示
