import urllib.request

import bs4

chapterNum = 1
chapter = "0" + str(chapterNum)
url = "http://www.glprogramming.com/red/chapter" + chapter + ".html"
while chapterNum < 15:
    if chapterNum < 10:
        chapter = "0" + str(chapterNum)
    else:
        chapter = str(chapterNum)
    url = "http://www.glprogramming.com/red/chapter" + chapter + ".html"
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    src = page.readall()
    parsed_html = bs4.BeautifulSoup(src)
    file = open("chapter" + chapter + ".html", "w")
    file.write(str(parsed_html))
    print("successfully got " + str(chapterNum))
    chapterNum += 1