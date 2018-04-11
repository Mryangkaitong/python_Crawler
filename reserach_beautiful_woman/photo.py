import urllib.request
import os
import re
def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    response=urllib.request.urlopen(url)
    html=response.read()
    return html

def get_page(url):
    b=[]
    html=url_open(url).decode('utf-8') 
    a=re.findall(r'\d{6}',html)
    return a[7]
    
def find_imgs(url):
    img_addrs=[]
    html=url_open(url).decode('utf-8')
    a=html.find('data-original="')
    b=html.find('.jpg',a,a+255)
    img_addrs.append(html[a+15:b+4])
    return img_addrs[0]
    

def save_imgs(folder,img_addrs,i,j=1):
    filname=str(i+1)+'.'+str(j)+'.jpg'
    with open(filname,'wb') as f:
        img=url_open(img_addrs)
        f.write(img)

def download_mm(folder='photo',pages=4,group=6):
    os.mkdir(folder)
    os.chdir(folder)
    url='http://www.tuwan.com/pic/'
    page_num=int(get_page(url))
    for i in range(pages):
        j=2
        page_num-=1
        page_url='http://www.tuwan.com/view/'+str(page_num)+'/'
        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs,i)
        for num in range(group-1):
            page_urlgroup='http://www.tuwan.com/view/'+str(page_num)+'_'+str(j)+'/'
            img_addrs=find_imgs(page_urlgroup)
            save_imgs(folder,img_addrs,i,j)
            j+=1
        
if __name__=='__main__':
    download_mm()
