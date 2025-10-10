phrase = 'PythonProgramming'
list_p = []
for p in phrase:
    if p not in list_p:
        list_p.append(p)
print(len(phrase) - len(list_p))
print("".join(list_p)) #リストの中身を1つの文字列に戻す。
#""は区切り文字がないことを意味するから
