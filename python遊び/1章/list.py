musician = ["RAD WIMPS","BUMP OF CHIKEN"]
print(musician)

#-------------------
locate = [(48.2,34.2),(57.2,13.4)]
print(locate)

#----------------
chara = {"身長":173,"好きな色":"オレンジ","作家":"武田双雲"}
print(chara)

#-----------------
k = input("キーを入力:")
if k in chara:
    value = chara[k]
    print(value)
else:
    print("そんなもんはねぇ")

#-----------------
chara = {
    "身長":173,"好きな色":"オレンジ","作家":"武田双雲",
    "RAD WIMPS":["魔法鏡","DADA","君と羊と青"],
    "BUMP OF CHIKEN":["天体観測","カルマ","虹を待つ人"]
    }
print(chara)
