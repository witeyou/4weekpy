
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
data=[]
path='./index.html'

starsno = []

with open(path,'r') as f:
    Soup = BeautifulSoup(f.read(),'lxml')
    imgs = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    desnum = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p')
    pics = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')


for tit,pic,star,img,des in zip(titles,pics,stars,imgs,desnum):
    info = {
        'title':tit.get_text(),
        'price':pic.get_text(),
        'star_number':5-len(list(star.find_all("span","glyphicon-star-empty"))),
        'image':img.get('src'),
        'describe':des.get_text()
    }
    print(info)
    data.append(info)




