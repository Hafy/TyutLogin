#encoding:utf-8
#from urllib import request,parse
import urllib2,cookielib,urllib
#import http.cookiejar
import re
import os
from bs4 import BeautifulSoup
#from pytesser import *
#from PIL import Image, ImageDraw, ImageFont, ImageFilter
#可以用的我们学校的校网 python2版本的

username='学号'
password='密码'  
while True:
    form={'secretCodeEnable':'on','role':1,'userName':username,'password':password,'secretCode':''}
    url='http://gsb.tyut.edu.cn/tyut/v2/index'
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu\
    Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    req=urllib2.Request(url,headers=headers)
   # opener.add_header(headers.items())
#resp=request.urlopen(req)
    resp=opener.open(url)
    data=resp.read().decode('utf-8')
    img_url='http://gsb.tyut.edu.cn'+re.findall(r'img id=\"secretCode\" src=\"(.+?)\"',data)[0]
    img_req=urllib2.Request(img_url,headers=headers)
    #img_resp=request.urlopen(img_req)
    img_resp=opener.open(img_req)
    img_data=img_resp.read()
    fd=open('checkcode.jpg','wb')
    fd.write(img_data)
    fd.close()
    form['secretCode']=raw_input('请输入验证码')
    post_data=urllib.urlencode(form)#.encode('utf-8')	    
    r=opener.open(url,post_data)
    result=r.read().decode('utf-8')
    #print result
    llist=re.findall(r'<span>.+?(\(\d+?\))',result)
#print(number)
    if llist==[]:
        username+=1
        password+=1
        continue        
#page=BeautifulSoup(result)
#print(page.find_all('li'))
#print(page)
#print(type(page))
    score_url='http://gsb.tyut.edu.cn/tyut/v2//xsxk/stuCkCj'
    score_req=urllib2.Request(score_url,headers=headers)
    score_resp=opener.open(score_req)
    page=score_resp.read().decode('utf-8')
    p_url=re.findall(r'<img.+?src=\"(.+?)\?',page)[0]
    #print p_url
    file_name=p_url.split('/')[-1]
#print(file_name==username)
    photo_url='http://gsb.tyut.edu.cn'+p_url
    p_req=urllib2.Request(photo_url,headers=headers)
    p_resp=opener.open(p_req)
    if not os.path.exists(os.path.join(os.getcwd(),'photos')):
        os.mkdir('photos')
    os.chdir('photos')
    fd=open(file_name,'wb')
    fd.write(p_resp.read())
    fd.close()
    username+=1
    password+=1
    os.chdir('../')

#fd=open('tyut.html','w')
#fd.write(result)
#fd.close()

#post_req=urllib.request.Request(url,data=post_data,headers=headers)
#post_resp=urllib.request.urlopen(post_req)
#print(post_resp.read().decode('utf-8'))
#print(form['secretCode'])
#print(resp.headers.values())
#print(resp.status)
