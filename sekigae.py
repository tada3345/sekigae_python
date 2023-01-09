#1 「モジュール」をimportする
import random
import time
import pandas as pd
# from google.colab import drive

# ドライブに接続する
# drive.mount('/content/drive', force_remount=True)

# csvを読んでデータをdata に入れる
# data = pd.read_csv('drive/My Drive/python/students.csv')

students = {
    "番号":[1,2,3,4,5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
          26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
    "姓":["相沢", "井田", "上田", "榎本", "小田", "山田", "伊藤", "大橋", 
         "山下", "佐々木", "鈴木", "吉田", "島田", "遠山", "土屋", "加藤", 
         "北原", "古川", "伊藤", "萩原", "坂口", "山崎", "池田", "小宮", "神戸", 
         "渡辺","山本", "早瀬", "金井", "山城", "丸谷", "北爪", "川口", "古本", 
         "二宮", "星野", "岡本", "長澤", "両津", "権"],
    "名":["松子","たか子","亜希子","梅子","幸子", "沙織", "綾子", "美紀", 
         "真由", "佐智子", "はるみ", "由紀", "裕子", "久美子", "梢", "夏樹", 
         "里美", "佐智子", "和江", "いずみ", "明美", "美幸", "まりあ", "亜由美", 
         "悦子", "みちよ", "知奈", "あずさ", "早紀", "久子", "由香", "桃子", 
         "香", "真紀", "美咲", "英恵", "富美子", "妙子", "喜美代", "絵理"],
    "せい":["あいざわ", "いだ", "うえだ", "えなもと", "おだ", "やまだ", 
          "いとう", "おおはし", "やました", "ささき", "すずき", "よしだ", 
          "しまだ", "とおやま", "つちや", "かとう", "きたはら", "ふるかわ", 
          "いとう", "はぎわら", "さかぐち", "やまざき", "いけだ", "こみや", 
          "かんべ", "わたなべ", "やまもと", "はやせ", "かない", "やましろ", 
          "まるたに", "きたずめ", "かわぐち", "ふるもと", "にのみや", "ほしの", 
          "おかもと", "ながさわ", "りょうつ", "こん"],
    "めい":["まつこ", "たかこ", "あきこ", "うめこ", "さちこ", "さおり",  
          "あやこ",  "みき",  "まゆ",  "さちこ",  "はるみ",  "ゆき",  "ゆうこ",  
          "くみこ",  "こずえ",  "なつき",  "さとみ",  "さちこ",  "かずえ", 
          "いずみ",  "あけみ",  "みゆき",  "まりあ",  "あゆみ",  "えつこ",  
          "みちよ",  "ともな",  "あずさ",  "さき",  "ひさこ",  "ゆか",  
          "ももこ",  "かおり",  "まき",  "みさき",  "はなえ",  "ふみこ",  
          "たえこ",  "きみよ",  "えり"],
    "near-sight":[1,0,0,1,0,1,0,0,1,0, 1,0,0,1,0, 1,0,0,1,0, 1,0,0,1,0, 1,0,0,1,
                  0, 1,0,0,1,0, 1,0,0,1,0]
}

data = pd.DataFrame(students)

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
    #学生番号のランダムな番号を取り除き、それをdataのplaceの値に入れる。
    data.loc[index,'place'] = numlist.pop(randP)

data = data.sort_values(by = 'place',ascending = True)

#コンソール出力
i = 0
print("\n=============================黒板==============================\n")
print("　　　　　　　　　　　　　　 教卓\n")
for index,item in data.iterrows():
    #空白を1桁の数字の場合は一つ設ける
    for _ in range(2-len(str(item["番号"]))):
        print(" ",end = "")
    #番号、空白名前を入力
    #print(str(item["番号"]) + " " + item["せい"],end = "",flush = True)
    print(str(item["番号"]) + " " + item["姓"],end = "",flush = True)
    #苗字のあとに1～3の空白を苗字の長さに応じて入れる
    for _ in range(4-len(item["姓"])):
        print("　",end = "")
    i += 1    
    #1.5秒のサスペンス
    time.sleep(0.5)
    # 6回繰り返して改行
    if i%6 == 0:
       print("\n")
    
print("\n=============================================================\n")
print("PYTHONは楽しい! 😍")