演示了urllib.request

对于网站会有针对 ip 的反爬取，可以采用代理的方式
-------->
详见std_video.py   line 13--15
<-------!

获取图片链接列表
-------->
详见std_video.py   line 17-29 get_image_url()
<-------!

下载图片到本地
-------->
详见std_video      line 34-37 dl_image()
<-------!

本地下载路径的填写
例如：
-------->
'E:\\download001\\0001.jpg'   ---------win下有效
= = = = = 
path = '/Users/Hou/Desktop/aaa/'
url='http://data.whicdn.com/images/224263340/superthumb.jpg'
path + url.split('/')[-2] + url.split('/')[-1]
<-------!
