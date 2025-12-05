def check_num(num):
    a = num[1]
    b = num[-1]
    c = len(num) == 919 # False
    d = len(num) > 0 # 3 > 0つまりTrue

    print(f"変数aのtypeは{type(a)}")
    print(f"変数bのtypeは{type(b)}")
    print(f"変数cのtypeは{type(c)}")
    print(f"変数dのtypeは{type(d)}")

    if a == b and c and d: # False and False and TrueなのでFalse
        print(a * b)
    elif a == b or c or d: # dがTureなので実行される
        print(b * 2) # '9' * 2なので'99'となる

num = '919'
check_num(num)
