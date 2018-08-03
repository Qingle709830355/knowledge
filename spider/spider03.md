# 使用多线程和多进程爬取全本《名侦探柯南》漫画并存储

## 1.未使用进程池进行异步爬取

```Python
from bs4 import BeautifulSoup as bs
from multiprocessing import Process
import os
import requests
import re
from threading import Thread
import time
import sys



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}


class ConanCartoon(object):
    """漫画信息爬取类"""
    def __init__(self):
        self.main_url = 'http://n5.1whour.com/'

    def get_tags(self, bs_req):
        """
        获取所有漫画标题
        :return: 所有标题链接
        """
        tags = bs_req.select('#comiclistn > dd > a:nth-of-type(1)')
        return tags

    def get_content(self, current_url):
        """
        获取标题链接中的漫画内容
        :param current_url: 当前页面的url
        :return: 本页图片的链接， 图片的后缀名， 下一页图片的连接
        """
        first_img_url = re.findall("document.write.*?<img.*?src='(.*?)'>.*?", str(current_url))  # 当前页面图片的链接, 返回的是一个列表
        if len(first_img_url) > 0:
            *_, img_url = first_img_url[0].split('"')  # 获取当前页面中漫画图片的url
            img = self.main_url + img_url  # 连接url
            *_, suffix = img.split('.')  # 获取图片的后缀名
            next_url = re.findall('</script.*?src="/ad/sc_soso.js">.*?<a.*?href="(.*?)"', str(current_url))  # 获取下一页的url
        else:
            img, suffix, next_url = '', '', []
        return img, suffix, next_url

    def insert_mongodb(self):
        """
        存入mongodb中
        """
        pass


def process_downloader(tags, func, i, main_url='http://comic.kukudm.com/'):
    """进程的tags"""
    print('第%s个进程启动' % i)
    dl_list = []
    for tag in tags:
        time.sleep(5)
        bs_current = bs_requests(main_url + tag.get('href'))  # 获取使用bs解析后的当前页面
        filename = '《%s》' % tag.string  # 连接文件名
        dl = Downloader(func=func, bs_current=bs_current, filename=filename, i=i)  # 构造一个下载类的对象
        dl.start()  # 启动线程
    for dl in dl_list:
        dl.join()  # 加上join是为了记录每个进程爬取的时间
    print('第%s个进程结束' % i)


class Downloader(Thread):
    """下载器， 继承了Thread"""
    def __init__(self, func, bs_current, filename, i=0, main_url='http://comic.kukudm.com', num=1):
        super().__init__()
        self.func = func  # func为一个，漫画爬取类构造的对象
        self.num = num  # 爬取到第几张图片
        self.bs_current = bs_current  # bs解析后的当前页面源码
        self.main_url = main_url  # 主要的url
        self.filename = filename  # 文件名
        self.i = i  # 进程数

    def run(self):
        try:
            os.mkdir(self.filename)  # 创建一个文件夹， 如果文件夹已经存在了，会抛出FileExistsError异常
        except FileExistsError as e:
            print('文件已经存在了')
        while True:
            # if not is_exists:
            tuple1 = self.func.get_content(self.bs_current)  # 当前页面的漫画的url， 后缀， 下一页的url
            if len(tuple1[2]):  # 如果存在下一页， 则执行
                print('第%s个进程的，%s书籍的, 第%s张图片开始下载' % (self.i, self.filename, self.num))
                self.bs_current = bs_requests(self.main_url + tuple1[2][0])  # 将当前页面源码变成下一页的源码
                if self.num < 10:
                    str1 = '0%s' % self.num
                else:
                    str1 = str(self.num)
                if not os.path.exists('%s/%s_%s.%s' % (self.filename, self.filename, str1, tuple1[1])):
                    # 如果不存在这张图片就保存图片，如果存在图片， 就不保存
                    with open('%s/%s_%s.' % (self.filename, self.filename, str1) + tuple1[1], 'wb') as f:
                        f.write(bs_requests(tuple1[0])[0].content)  # requests.content 返回二进制， requests.text 返回文本
                    print('第%s个进程的%s书籍的, 第%s张图片下载结束' % (self.i, self.filename, self.num))
                else:
                    print('该图片已经下载过了!')
                self.num += 1
                time.sleep(5)
            else:
                print('%s下载完成！' % self.filename)
                time.sleep(5)
                break


def bs_requests(url):
    """
    返回请求的页面， 以及解析后的页面源码
    :param url:  url
    :return: 返回请求的页面， 以及解析后的页面源码
    """
    req = requests.get(url=url, headers=HEADERS)  # 请求页面
    req.encoding = 'gbk'  # 解码源码
    bs_req = bs(req.text, 'html5lib')  # 使用bs4解析页面
    return req, bs_req


def main():
    sys.setrecursionlimit(100000)  # 设置系统的递归深度
    url = 'http://comic.kukudm.com/comiclist/5/'
    bs_req = bs_requests(url)[1]
    conan = ConanCartoon()  # 构造一个ConanCartoon对象
    tags = conan.get_tags(bs_req)  # 获取所有标题
    num = len(tags)//5
    title_num = 0
    end_num = 0
    for i in range(5):
        if i + 1 != 5:
            div_tags = tags[title_num: (num + end_num)]
            Process(target=process_downloader(tags=div_tags, func=conan, i=i+1)).start()
            title_num += num
            end_num += num

        else:
            div_tags = tags[title_num:]
            Process(target=process_downloader(tags=div_tags, func=conan, i=i+1)).start()


if __name__ == '__main__':
    main()

```



## 2.使用进程池进行异步爬取



