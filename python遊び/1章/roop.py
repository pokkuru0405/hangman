##shows = ["an","dv","dd"]
##for show in shows:
##    print(show)
##
##x = 25
##while x <= 50:
##    print("{}".format(x))
##    x += 1
##
##
##shows = ["an","dv","dd"]
##for index,show in enumerate(shows):
##    print(index)
##    print(show)
##
##x = 25
##while x <= 50:
##    print("{}".format(x))
##    x += 1

##shows = ["1","2","3","4","5","6","7","8"]
##while True:
##    a = input("文字を入力してください:")
##    if "q" == a:
##        print("qのため終了します．")
##        break
##    elif a in shows :
##        print("正解，終了します")
##        break
##    else:
##        print("数字を入力するか，qで終了します．")
##

a = [1,2,3]
b = [1,2,3]
new = []

for i in a:
    for j in b:
        new.append(i*j)

print(new)
