colors = '赤:青:黄' # 赤、青、黄を代入する
parts = colors.split(':') # 結果をリストpartsに代入
number = len(colors) # 結果をnumberに代入する
print(parts[1] + number * parts[2]) # 結果を出力
