from bs4 import BeautifulSoup
import requests
import time

url_00='http://bj.xiaozhu.com/fangzi/4637053514.html'
url_01='http://bj.xiaozhu.com/search-duanzufang-p1-0/'


def get_info(url,data=None):
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    titles=soup.select('div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address=soup.select('div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    prices=soup.select('#pricePart > div.day_l > span')
    imgs_home=soup.select('#curBigImage')
    sexs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    names=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    imgs_master=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    for title,addres,price,img_home,sex,name,img_master in zip(titles,address,prices,imgs_home,sexs,names,imgs_master):
        if (sex.get('class') == ['member_ico1']):
            ture='woman'
        else:
            ture='man'
        data={
            'title'   :title.get_text(),
            'addres'  :addres.get_text(strip=True),
            'price'   :price.get_text(),
            'img_home':img_home.get('src'),
            'sex':ture,
            'name'    :name.get_text(),
            'img_master':img_master.get('src'),
        }
    print(data)
#get_info use to get every page's infomation

def get_link(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    linkss=soup.find_all("a","resule_img_a",target='_blank')
    web_links=[]
    for links in linkss:
        web_links.append(links.get('href'))
    #print(web_links[0:-1])
    return web_links
#return a list include some wed's links

for i in get_link(url_01):
    print('this is page:' + i + '\n')
    get_info(i)
