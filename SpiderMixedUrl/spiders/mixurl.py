# coding=utf8

import scrapy
from urllib.parse import urlparse
from SpiderMixedUrl.items import SpidermixedurlItem


class MixUrl(scrapy.Spider):
    name = 'mix'
    allowed_domains = ['*']
    # 'http://c.biancheng.net/cplus/', 'https://www.oschina.net/p/python', 'https://www.oracle.com/java/technologies/javase-jdk8-downloads.html', 'https://www.zhihu.com/question/50795063'
    start_urls = [
        'https://www.cplusplus.com/reference/',
        'https://xkcd.com/353/',
        'https://realpython.com/',
        'https://www.kaggle.com/learn/python',
        'https://www.quora.com/What-is-C+-as-opposed-to-C++',
        'https://cplusarchitects.net/',
        'https://www.tutorialspoint.com/objective_c/index.htm'
        
        'https://learnxinyminutes.com/docs/objective-c/',
        'https://www.goodfirms.co/glossary/objective-c/',
        'https://www.tiobe.com/tiobe-index/objective-c/',
        'https://www.tutorialspoint.com/objective_c/index.htm',
        'http://cpp.sh/',
        'https://isocpp.org/',
        'https://www.coursera.org/learn/c-plus-plus-a',
    ]

    custom_settings = {
        'LOG_FILE': None,
        'DEFAULT_REQUEST_HEADERS': {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        },
        'IMAGES_STORE': None,
        'IMAGES_THUMBS': None,
        'DOWNLOADER_MIDDLEWARES': {},
        'ITEM_PIPELINES': {},
    }

    ret_href = []

    def parse(self, response):
        url = urlparse(response.url)
        if not url:
            return None
        host = '{0}://{1}'.format(url.scheme, url.netloc)
        list_href = response.xpath('//a/@href').extract()

        if not list_href or not isinstance(list_href, list):
            return None

        for i in list_href:
            items = SpidermixedurlItem()
            if i in self.ret_href:
                continue
            if not i.startswith('http'):
                x_url = '{host}.{path}'.format(host=host, path=i)
                self.ret_href.append(x_url)
                items['url'] = x_url
            elif i.startswith('http'):
                self.ret_href.append(i)
                items['url'] = i
            else:
                pass

            yield items



