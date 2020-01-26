'''
whois域名信息收集器
'''
# 导入requests模块，bs4模块里的BeautifulSoup，time模块
import requests
from bs4 import BeautifulSoup
import time
# 设置开始时间点
start = time.time()


def chax():
    # 询问查询的域名
    domain = input('请输入你要查询的域名:')
    # 设置浏览器头通过反爬
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    # 设置url
    url = "http://site.ip138.com/{}/".format(domain)
    urlDomain = "http://site.ip138.com/{}/domain.htm".format(domain)
    url2 = "http://site.ip138.com/{}/beian.htm".format(domain)
    url3 = "http://site.ip138.com/{}/whois.htm".format(domain)
    # 访问网页
    rb = requests.get(url, headers=head)
    rb1 = requests.get(urlDomain, headers=head)
    rb2 = requests.get(url2, headers=head)
    rb3 = requests.get(url3, headers=head)
    # 获取内容并用html的方式返回
    html = BeautifulSoup(rb.content, 'html.parser')
    print('IP解析目录')
    # 读取内容里的p标签
    for x in html.find_all('p'):
        # 返回text内容
        text = x.get_text()
        print(text)
    html1 = BeautifulSoup(rb1.content, 'html.parser')
    print('子域名查询')
    for v in html1.find_all('p'):
        text1 = v.get_text()
        print(text1)
    html2 = BeautifulSoup(rb2.content, 'html.parser')
    print('备案查询')
    for j in html2.find_all('p'):
        text2 = j.get_text()
        print(text2)
    html3 = BeautifulSoup(rb3.content, 'html.parser')
    print('whois查询')
    for k in html3.find_all('p'):
        text3 = html3.get_text()
        print(text3)


chax()
end = time.time()
print('查询耗时:', end - start)
