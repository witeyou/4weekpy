import requests
from bs4 import BeautifulSoup
import urllib.request
import time

wed_url_base = 'http://www.hacg.ch/wp/category/all/anime/page/'
path = 'E:/download001/'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36','Cookie':'__cfduid=d9b40524b69d8507d13a5d3622852ee5a1508677791; _gat=1; _ga=GA1.2.191156083.1508677794; _gid=GA1.2.1534465407.1508677794'}


def get_imgs_url(endnum):
    img_links=[]
    for page_num in range(1,endnum):
        wed_url_full=wed_url_base+str(page_num)
        web_data=requests.get(wed_url_full,headers=header)
        soup=BeautifulSoup(web_data.text,'lxml')
        imgs=soup.find_all("img","aligncenter")
        time.sleep(2)
        for i in imgs:
            img_links.append(i.get('src'))
    print((len(img_links)),'images shall be downloaded!')
    return img_links

'''
def dl_image(url):
    urllib.request.urlretrieve(url, path)
    print('Done')
'''
for url in get_imgs_url(3):
    print(url)

print('All work is done')
