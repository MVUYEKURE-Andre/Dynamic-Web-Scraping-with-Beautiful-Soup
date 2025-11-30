# from bs4 import BeautifulSoup
# import requests
# with open("website.html") as file:
#     content=file.read()
#     # print(content.title())
# soup=BeautifulSoup(content,"html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.)
# # heading=soup.find_all(name="h3",class_="heading")
# # print(heading)
# # company_url=soup.select_one(selector="p a")
# # print(company_url)
# headings=soup.select_one(selector=".heading")
# print(headings)

from bs4 import BeautifulSoup
import requests
response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.fin)
soup=BeautifulSoup(response.text,"html.parser")
# print(soup.title)
headings=soup.find_all(name="h3",class_="title")
move_heading=[heading.getText() for heading in headings]
move_heading.reverse()
move_tit_hed=[]
for move in move_heading:
    with open("bestmove", "a", encoding="utf-8") as topmove:
        topmove.write(move+ "\n")

