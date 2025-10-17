a = 17
b = 5
dm = divmod(a, b)
p = pow(dm[0], dm[1])
all_num = [a, b, dm[0], dm[1], p]
min_all = min(all_num)
max_all = max(all_num)
sum_all = sum(all_num)

print(f'{min_all}, {max_all}, {sum_all}')

print(all_num)
