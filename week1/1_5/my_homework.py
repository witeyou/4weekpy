from bs4 import BeautifulSoup
import requests
import time

#full_url='http://bj.58.com/pbdnhuashuo/0/pn2/'
url_base='http://bj.58.com/pbdnhuashuo/0/pn'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

def get_weblinks (endpage):
    link_to = []
    for page in range(1,endpage+1):
        full_url=url_base+str(page)
        web_data_1=requests.get(full_url,headers=header)
        web_data_1_soup=BeautifulSoup(web_data_1.text,'lxml')
        links_to=web_data_1_soup.find_all("a","t",target="_blank",rel="nofollow")
        for link in links_to:
            link_to.append(link.get('href'))
    return link_to
#return a list have links to the childweb
#problem the links returned is wrong

def get_info (url):
    web_data_1=requests.get(url,headers=header)
    web_data_1_soup=BeautifulSoup(web_data_1.text,'lxml')
    title=web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1')[0].get_text(strip=True)
    time=web_data_1_soup.select('#index_show > ul.mtit_con_left.fl > li.time')[0].get_text(strip=True)
    price=web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(1) > div.su_con > span')[0].get_text(strip=True)
    newpercent=web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')[0].get_text(strip=True)
    if (web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span > a'))!=[]:
        addres=web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span > a')[0].get_text(strip=True)
    else:addres='unknown'
    #this if sentence reliize the state when address is none   and remind us soup.select return a list
    web_info={
        'title':title,
        'time':time,
        'price':price,
        'newprecent':newpercent,
        'address':addres
    }
    return web_info
#get_info be used to get a page's info and return a dict own these info

#line 45-47 only be uesed check out
url_test='http://bj.58.com/pingbandiannao/31284313175373x.shtml?adtype=1&PGTID=0d3065ea-0000-130d-b28d-475ae0ad3a77&entinfo=31284313175373_0&psid=191218713197768391341070136&iuType=_undefined&ClickID=3'
url_test1='http://bj.58.com/pingbandiannao/31616458602313x.shtml?adtype=1&PGTID=0d3065ea-0000-18e1-e3ee-ed341b9ee66c&entinfo=31616458602313_0&psid=153908153197776798959654712&iuType=_undefined&ClickID=3'
web_links_test=[url_test,url_test1]

web_infos=[]
for i in web_links_test:
    web_infos.append(get_info(i))
    time.sleep(2)
print(web_infos)

'''
for i in get_weblinks(1):
    #web_infos.append(get_info(str(i)))
    print(get_info(str(i)))
    time.sleep(2)
print(web_infos)
'''
print('All work is done')

