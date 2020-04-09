
抓取指定 url地址上的所有超链接，未做深层次抓取。


执行方法：

进入 SpiderMixedUrl\SpiderMixedUrl：

执行：scrapy crawl mix -o xxx.csv 

将爬取的url链接 写入到同目录下的 xxx.csv 里面。


附：
-o 支持的文件后缀： ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')