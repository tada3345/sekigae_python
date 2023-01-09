#1 「モジュール」をimportする
import random
import time
import pandas as pd
from google.colab import drive

# ドライブに接続する
drive.mount('/content/drive', force_remount=True)

# csvを読んでデータをdata に入れる
data = pd.read_csv('drive/My Drive/python/students.csv')

# 学生数をstuSumに入力 
stuSum = len(data)
# 学生数をリスト化してnumlistに入力
numlist = list(range(stuSum))

# dataにplaceという項目を追加して0を入れる
data['place'] = 0 

#dataを一列づつループ処理
for index,item in data.iterrows():
    # ランダムの番号をrandPに入力
    randP = random.randint(0,len(numlist)-1)#要素番号をランダムで指定
    #近視の人は下の処理
    if item['near-sight']:
            # 生徒数÷２-1までの数でランダムの番号をrandPに入力？　36人なら　1-17の番号
        randP = random.randint(0,int(len(numlist)/2-1))#近視の人は前の方から指定
    #学生番号のランダムな番号を取り除き、それをdataのplaceの値にindexの値と共に入れる。
    data.loc[index,'place'] = numlist.pop(randP)

data = data.sort_values(by = 'place',ascending = True)

#コンソール出力
i = 0
print("\n=============================黒板==============================\n")
print("　　　　　　　　　　　　　　 教卓\n")
for index,item in data.iterrows():
    #空白を1桁の数字の場合は一つ設ける
    for _ in range(2-len(str(item["席"]))):
        print(" ",end = "")
    #番号、空白名前を入力
    print(str(item["席"]) + " " + item["姓"],end = "",flush = True)
    #苗字のあとに1～3の空白を苗字の長さに応じて入れる
    for _ in range(4-len(item["姓"])):
        print("　",end = "")
    i += 1    
    #1.5秒のサスペンス
    time.sleep(0.09)
    # 6回繰り返して改行
    if i%6 == 0:
        print("\n")
    
print("\n=============================================================\n")
print("PYTHONは楽しい! 😍")