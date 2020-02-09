##a = []
##with open("おちんちん.txt","r",encoding="utf-8") as f:
##    a.append(f.read())
##
##print(a)

##ans = input("どんなおちんちんがすきですか:")
##
##with open("おちんちん.txt","w",encoding="utf-8") as f:
##    f.write(ans)

##import csv
##
##with open("chi.csv","w") as f:
##          w = csv.writer(f,delimiter=",")
##          w.writerow(["chi","chin","chinchi"])
##          w.writerow(["chi2","","chinchi2"])
##          w.writerow(["chi3","chin3","chinchi3"])
##          
import csv

movies = [["ちんこ", "ちんちん", "Minority Report"], ["ちんぽこ", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
