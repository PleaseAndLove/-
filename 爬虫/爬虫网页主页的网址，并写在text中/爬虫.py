import urllib.request
from bs4 import BeautifulSoup
'''
        用于爬取site网页的网址，
        使用时向Scraper传递网址参数，
        只能处理一个网页
'''


class Scraper:
    def __init__(self, site):
        self.site = site
        self.site_list = []

    def scrape(self):
        if 1:
            r = urllib.request.urlopen(self.site)
            html = r.read()
            parser = 'html.parser'
            sp = BeautifulSoup(html, parser)
            for tag in sp.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                if 'html' in url:
                    print('\n'+ url)
                    self.site_list.append(url)
            with open('baidu_new_site.txt', 'w') as f:
                f.write(str(self.site_list))
    

new = 'https://news.baidu.com/'
Scraper(new).scrape()

