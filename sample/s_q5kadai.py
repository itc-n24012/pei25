list_a = [5, 12, 7, 12, 20] # list_aリストを作成

list_b = list_a.copy() #copyでlist_bを作成
list_b.remove(12) # 12を1つだけ削除
list_b.insert(2, 99) # 99を挿入
list_b.append(0) # 末尾に0を追加

print("list_a:", list_a)
print("list_b:", list_b)
