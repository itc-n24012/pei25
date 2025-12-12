a = -100
b = 10

if a < 0 and b < 0 and a > b: # False
    c = a + b
    d = '有効な数字ではありません'
elif (a < 0 and b < 0) or a > b: # False
    c = a / b
    d = '有効な数字ではありません'
elif (a < 0 or b < 0) and a > b: # False
    c = a + b
    d = a > b
else: # ここが実行される
    c = a / b # -10.0
    d = a > b # False

print(f'{type(c)} {type(d)}')
