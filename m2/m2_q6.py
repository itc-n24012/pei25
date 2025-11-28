def fukuri(ganpon, nenri, nensu): # 複利
    zandaka = ganpon * 10000
    for i in range(nensu):
        zandaka += zandaka * nenri 
    return int(zandaka)

def tanri(ganpon, nenri, nensu): # 単価
    zandaka = ganpon * 10000
    for i in range(nensu):
        zandaka += ganpon * 10000 * nenri
    return int(zandaka)

def hikaku(ganpon, nenri, nensu): # 比較
    print(f'元本{ganpon}万円, 年利{nenri:.0%}で{nensu}年間預けた場合') # {nenri:.0%}について、nenriをパーセント表示に変更5%と表示
    fu = fukuri(ganpon, nenri, nensu) / 10000 # 複利の残高を万単位 
    ta = tanri(ganpon, nenri, nensu) / 10000 # 単利の残高を万単位
    print(f'複利の方が{fu - ta: .1f}万円多く受け取ることができます') # .1fは少数第一位まで表示

def hitsuyou_nensu(ganpon, nenri, uketori): # 必要年数
    print(f'年利{nenri:.0%}で利子を{uketori}万円受け取るには')
    kaku_f = 0 # 繰り返し判定に使う利息を格納しておく変数
    year_f = 0 # fukuriの年カウント用変数
    while kaku_f < uketori * 10000:
        kaku_f = fukuri(ganpon, nenri, year_f + 1) - ganpon * 10000 # 複利での元利合計から元本を引き、利息だけを計算
        year_f += 1 # year_fのカウント
    kaku_t = 0 # 繰り返し判定に使う利息を格納しておく変数
    year_t = 0 # tanriの年カウント用変数
    while kaku_t < uketori * 10000:
        kaku_t = tanri(ganpon, nenri, year_t + 1) - ganpon * 10000 # 複利での元利合計から元本を引き、利息だけを計算
        year_t += 1 # year_tのカウント
    print(f'複利で{year_f}年、単利で{year_t}年かかります')

hikaku(100, 0.05, 10)
hitsuyou_nensu(100, 0.05, 300)
