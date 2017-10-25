

爬连接时也可以使用find_all()
-------->
links_to=web_data_1_soup.find_all("a","t",target="_blank",rel="nofollow")
#取自my_homework line 15
<-------!


处理了爬页面上时可能面临的部分数据格式不同或丢失的情况
-------->
if (web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span > a'))!=[]:
        addres=web_data_1_soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span > a')[0].get_text(strip=True)
else:addres='unknown'
#利用了IF语句进行判断 依据是如果select()数据为空，那么返回的会是一个空的list。
<-------!


通过split()把字符裁剪提取
-------->
urls.append(link.get('href').split('?')[0])
#取自std_homework line 16
#split(str)方法会返回一个list,str是分割的标志
<-------!


通过查询接口来获取信息
-------->
def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    # 这个是找到了58的查询接口，不了解接口可以参照一下新浪微博接口的介绍
    js = requests.get(api)
    views = js.text.split('=')[-1]
    return views
#取自std_homework line 20-26	
<-------!