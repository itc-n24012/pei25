def adjust_recipe(recipe_kosaji, recipe_servs, cook_servs): # レシピの小さじ料を、作る分量に合わせて調節する関数
    adjust_kosaji = recipe_kosaji * (cook_servs / recipe_servs) # 基準レシピの小さじ量*(作る人数/レシピの人数)
    return adjust_kosaji

def round_kosaji(adjust_kosaji): # 小さじの量を0.5刻みに丸める関数
    int_part = int(adjust_kosaji) # 整数部分
    frac_part = adjust_kosaji - int_part # 小数部分
    if frac_part >= 0.5:
        return str(int_part) +  '.5' # 0.5以上なら「.5」にする
    else:
        return str(int_part) # それ以上は整数のまま

recipe_servs = int(input('レシピは何人前？: ')) # レシピが何人前か入力

saji_type = '' # 大さじか小さじかを正しく入力するまで繰り返す
while saji_type not in ['L', 'S']:
    saji_type = input('レシピのさじの種類は？ (大さじはL, 小さじはS) : ')

saji_name = '大さじ' if saji_type == 'L' else '小さじ' # 選択に応じて表示名を決定
recipe_saji = float(input(f'レシピは{saji_name}何杯？: ')) # レシピのさじの量を入力

cook_servs = int(input('作る料理は何人前？: ')) # 実際に作る人数を入力

recipe_kosaji = recipe_saji * 3 if saji_type == 'L' else recipe_saji # 入力が大さじの場合は小さじ換算(大さじ1 = 小さじ3)
adjust_kosaji = adjust_recipe(recipe_kosaji, recipe_servs, cook_servs) # 作る人数に合わせて小さじ換算量を調節

cook_oosaji, cook_kosaji = divmod(adjust_kosaji, 3) # 小さじ量を「大さじ」と「小さじ」に分解(小さじ3で大さじ1)

print(f'{cook_servs}人前では、大さじが{cook_oosaji:.0f}杯と小さじが{round_kosaji(cook_kosaji)}杯です。')

