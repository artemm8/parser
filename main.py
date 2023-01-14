from email import parser
from turtle import title

import requests
from bs4 import BeautifulSoup
def pars(url,class_n,page,file):
    with open(file,"w",encoding="UTF-8") as f:
        for g in range(1,page+1):
            responds=requests.get(f"{url}{g}/")
            startgamer=responds.content
            html=BeautifulSoup(startgamer,"html.parser")
            game=html.find_all(class_=class_n)
            print(g)
            


            for i in game:
                print(i.text)
                f.write(i.text+" "+i.a.attrs["href"]+"\n")

url=input("Введите Ссылку ")
title_site=input("Введите класс ")
page=int(input("Введите количеста страниц "))
file=input("Введите название файла ")
pars(url,title_site,page,file)