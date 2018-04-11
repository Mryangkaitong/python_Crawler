import urllib.request
import random
url='http://www.whatismyip.com.tw'

iplist=['39.137.46.78:8080']

proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)

html=response.read().decode('utf-8')

print(html)
