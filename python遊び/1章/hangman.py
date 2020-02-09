def hangman(word):
    wrong = 0
    stages = ["",
              ""_________    "
              ""|            ",
              ""|            ",
              ""|   O",
              ""|   ｜       ",
              ""|   ｜       ",
              ""|   /|       ",
              ""|            ",
              ""|            "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    wind = False
    print("ハングマンへようこそ")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
