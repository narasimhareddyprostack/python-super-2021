from bs4 import BeautifullSoup4
import requests

response = requests.get("https://www.imdb.com/list/ls003992425/")
source = response.text

soup = BeautifullSoup(source, "lxml")

tags = soup.find_all("a")
list = []
for tag in tags:
    try:
        if tag["href"].startswith("/title/tt"):
            if tag.text != " ":
                list.append(tag.text)

    except:
        pass
	 
no=0
i=0	 
for movie in list:
    no = no + 1
    if no%2 ==0:
        i +=1
        print(i, movie)  