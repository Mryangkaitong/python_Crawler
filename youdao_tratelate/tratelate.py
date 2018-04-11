import urllib.request
import urllib.parse
import random
import json
#这里是用了代理ip(注意最好用谷歌去找国外的代理ip)
iplist=['39.137.46.78:8080']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener=urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
#这里是爬虫有道翻译
while True:
    content=input('请输入需要翻译的内容：')
    if content=='q!':
        break
    url='http://fanyi.youdao.com/translate'
    data={}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='1523277981766'
    data['sign']='cc8f86230aa8478163b58bdbd7c3cdb6'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_REALTIME'
    data['typoResult']='false'
    data=urllib.parse.urlencode(data).encode('utf-8')
    req=urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')

    target=json.loads(html)

    print("翻译结果就是：%s" % (target['translateResult'][0][0]['tgt']))


    
