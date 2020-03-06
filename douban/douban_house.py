"""
Reference：
https://blog.csdn.net/gmr2453929471/article/details/78556898
https://blog.csdn.net/sinat_37812785/article/details/104247874
"""
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import csv


# 模拟浏览器环境，防止被反爬虫机制拦截
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


start = 0
end = 10
page_size = 25
group_ids = []
key_words = []

href_start = 18
href_end = 63
title_start = 72

out_file = open("douban_house_result.csv", "w+", encoding='gb18030')
csv_writer = csv.writer(out_file, lineterminator='\n')

# parameters

_POSTER_BLACKLIST = {

}

_KEYWORD_BLACKLIST = {

}


class DoubanHousing(object):
    """
    Get latest apartment renting information form "Douban Group"
    Features:
        - Get information from more than one group
        - Complex search condition supported
        - Filters
            . Posting time
            .
    """
    def __init__(self, group_ids=None, key_words=[]):
        if group_ids is None:
            # set search range to the entire Douban group
            NotImplementedError
        self.keywords = key_words
        

    def _property_parsing(self):
        """
        Parse apartment properties from title and post
        :return:
        """



def crawl_douban_room():
    for i in range(end):
        print(i)
        url = "https://www.douban.com/group/145219/discussion?start="+str(i*25)
        req = urllib.request.Request(url, headers=headers)
        req = urllib.request.urlopen(req)
        response = req.read()
        soup = BeautifulSoup(response, "html5lib")
        info = soup.select("table.olt tbody tr")
        for child in info[1:]:
            content = child.select("td.title a")[0].prettify().encode('utf-8')
            href = content[href_start:href_end]
            title_end = content.find(b'">')
            title = content[title_start:title_end]
            for key_word in key_words:
                if title.find(key_word.encode()) != -1:
                    csv_writer.writerow([href.decode(), title.decode('utf-8')])
                    break


if __name__=="__main__":
    crawl_douban_room()

