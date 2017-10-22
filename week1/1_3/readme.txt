演示了 bs4 request time库

format用法--------->
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
<---------!

headers用法--------->
headers = {
    'User-Agent':'',
    'Cookie':''
}
<----------!
利用伪造headers 假装手机端访问网页------->
std_code.py line 54-65
<-------


time用法-------->
std_code.py line 17
<-------

soup.XXX 寻找网页中元素的方法：
titles    = soup.select('div.property_title > a[target="_blank"]')
imgs      = soup.select('img[width="160"]')
cates     = soup.select('div.p13n_reasoning_v2')
titles    = soup.select('a.location-name')
imgs      = soup.select('div.photo > div.sizedThumb > img.photo_image')
metas     = soup.select('span.format_address')
linkss    =soup.find_all("a","resule_img_a",target='_blank')

修饰网页中元素的方法
'title'  :title.get_text(),
'img'    :img.get('src'),
'meta'   :list(meta.stripped_strings)



