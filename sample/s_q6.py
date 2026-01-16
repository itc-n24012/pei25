import random # shuffleやrandintで利用
import sys # sys.exit()利用する

words = [('apple', 'りんご'), ('banana', 'バナナ'),
         ('coconut', 'ココナッツ'), ('doughnut', 'ドーナツ'),
         ('effort', '努力'), ('future', '未来'), ('gorilla', 'ゴリラ'),
         ('house', '家'), ('information', '情報'), ('journey', '旅')]

questions = int(input('出力数を入力:'))

length = len(words) # lengthに代入
if length < questions: # questionsが登録されている単語数より大きい場合は終了
    print('登録された単語数以下の数値を入力してください。')
    sys.exit()

count = 0 # 出題済みの問題をカウントする変数
correct = 0 # 正解数を表示させる

while count < questions:
    random.shuffle(words) # 中身をシャッフル
    ans_index = random.randint(0, 3) # 0~3の中からランダムに1つの整数を選んでans_indexに代入する
    print(f'問題{count + 1}:{words[ans_index][0]}の意味は？') # 問題分を表示する処理

    for i in range(2): # 同じ処理を2回繰り返す
        print(f'{i * 2 + 1}:{words[i * 2][1]}, {i * 2 + 2}:{words[i * 2 + 1][1]}') # 選択肢の出力を2回のループで行う

    answer = input('1から4の数字で解答 (終了する場合は"x"を入力) :')
    if answer == 'x': # xが入力されたらループ終了
        break

    print(f'あなたの解答:{answer}')
    if answer == str(ans_index + 1): # 入力された答えが正解番号と一致するかを確認
        print('正解!')
        correct += 1
    else:
        print(f'不正解! 正解は{ans_index + 1}の{words[ans_index][1]}でした!')

    count += 1 # 次の問題のカウントを進める

print(f'成績:正解{correct}問 (全{count}問) ') # 成績の表示

