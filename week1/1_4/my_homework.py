import requests
from bs4 import BeautifulSoup
import urllib.request
import time

wed_url_base = 'http://www.hacg.ch/wp/category/all/anime/page/'
path = 'E:\\download001\\'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

def get_imgs_url(endnum):
    img_links=[]
    for page_num in range(1,endnum):
        wed_url_full=wed_url_base+str(page_num)
        #web_data = requests.get(wed_url_full)
        web_data=requests.get(wed_url_full,headers=header)
        soup=BeautifulSoup(web_data.text,'lxml')
        imgs=soup.find_all("img","aligncenter")
        time.sleep(2)
        for i in imgs:
            img_links.append(i.get('src'))
    print((len(img_links)),'images shall be downloaded!')
    return img_links


def dl_image(aurl):
    urllib.request.urlretrieve(aurl,path + aurl.split('/')[-2] + aurl.split('/')[-1])
    print(path+ aurl.split('/')[-2] + aurl.split('/')[-1])

for url in get_imgs_url(3):
    dl_image(url)
    print(url)

print('All work is done')

#运行失败有反爬虫处理