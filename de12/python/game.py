score = 0
print ("都道府県当てクイズ！")
print("どの都道府県か当ててみよう！") 
print("漢字で答えてください")

a = input("日本で一番広い面積をもつ場所は？")
if a =="北海道" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

b = input("日本で一番人口が少ないのは？")
if b =="鳥取県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

c = input("日本で最も面積が小さいのは？")
if c =="香川県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

d = input("伊勢神宮があるのは？")
if d =="三重県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

e = input("坂本龍馬が生まれたのは？")
if e =="高知県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

f = input("出雲大社があるのは？")
if f =="島根県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

g = input("阿波踊りで有名なのは？")
if g =="徳島県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

h = input("軍艦島があるのは？")
if h =="長崎県"  :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

i = input("太宰府天満宮があるのは？")
if i =="福岡県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

j = input("日光東照宮があるのは？")
if j =="栃木県" :
    print("正解！")
    score = score + 1
else : 
    print("不正解！")

print(score,"門正解！")
print("正答率は",score /10*100,"％でした！")