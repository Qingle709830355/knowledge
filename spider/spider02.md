# 使用requests+bs4多线程爬取智联招聘和boss招聘职位信息

```Python
# boss直聘 https://www.zhipin.com/job_detail/?query=python&scity=101010100
# 智联招聘 https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=python&p=2
from bs4 import BeautifulSoup as bs
import csv
from threading import Thread
import requests
from urllib import parse


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}


def get_html(url):
    """
    获取bs解析的源码
    :param url:  需要爬取页面的url
    :return:  返回bs解析后的源码
    """
    req = requests.get(url=url, headers=HEADERS)  # requests请求页面
    req_bs = bs(req.text, 'html5lib')  # bs解析， 后面的html5lib是设置解析的方法， 还可以选择lxml
    return req_bs


def get_content(html, selector):
    """
    获取所有职位的内容
    :param html: bs解析后的源码
    :param selector: css选择器
    :return: 返回所有职位
    """
    all_li = html.select(selector)
    return all_li


def get_boss_job(one_html):
    """
    boss直聘网站上的单个职位信息的各个部分
    :param one_html:  一个综合的职位信息
    :return: 返回公司名称， 职位信息， 薪资， 职位链接， 工作地点和要求
    """
    bs_html = bs(str(one_html), 'html5lib')
    a_href = 'https://www.zhipin.com' + bs_html.find('a').get('href')
    title = bs_html.find('div', class_='job-title').string
    salary = bs_html.find('span', class_='red').string
    p = bs_html.find('p').text
    name = bs_html.select_one('div.info-company > div > h3 > a').string
    return name, title, salary, a_href, p


def get_zhilian_job(one_html):
    """
    爬取智联招聘各个职位要求的元组
    :param one_html: 单个职位的综合源码
    :return: 返回公司名字， 职位需求， 薪资， 工作地点和要求
    """
    bs_html = bs(str(one_html), 'html5lib')
    need = bs_html.select_one('td.zwmc > div > a').text
    need_href = bs_html.select_one('td.zwmc > div > a').get('href')
    name = bs_html.select_one('td.gsmc > a').text
    salary = bs_html.select_one('td.zwyx').text
    p = bs_html.select_one('td.gzdd').text
    return name, need, salary, need_href, p


class PythonJob(Thread):
    """爬取并写入csv文件的线程类"""
    def __init__(self, url, selector, name):
        super().__init__()
        self._url = url  # 需要爬取的url
        self._selector = selector  # css选择器
        self._name = name  # 文件文字

    def run(self):
        print('线程开始')
        html = get_html(self._url)  # 获取源码
        html_list = get_content(html, self._selector)  # 爬取所有职位的综合信息
        job_list = []
        dict1 = {'1': 'bossjob', '2': 'zhilianjob'}  # 爬取的不同网站的名字
        for num, one_html in enumerate(html_list):
            if self._name == '1':
                if all(list(get_boss_job(one_html))):  # 判断爬取的职位所有信息的元组是否为空， 为空，就跳出for循环
                    job_list.append(list(get_boss_job(one_html)))
                else:
                    break
            if self._name == '2':
                if num > 0:
                    if all(list(get_zhilian_job(one_html))):
                        job_list.append(get_zhilian_job(one_html))
                    else:
                        break
        with open('pythonjob/%s.csv' % dict1[self._name], 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['公司名字', '职位需求', '职位薪资', '职位链接', '工作地点和要求'])
            writer.writerows(job_list)
        print('线程结束')


if __name__ == '__main__':
    city = input('请输入城市：')
    job = input('请输入职位：')

    # search2 = parse.urlencode({'jl': city, 'kw': job, 'p': page})
    url_dict = {
        1: 'https://www.zhipin.com/c101010100/h_101010100/?',
        2: 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
    }
    for i in range(1, 20):
        search1 = parse.urlencode({'query': job, 'page': i, 'ka': 'page%s' % i})
        selector1 = 'div.job-list > ul > li'
        url1 = url_dict[1] + search1
        search2 = parse.urlencode({'jl': city, 'kw': job, 'p': 1})
        selector2 = 'div.newlist_list_content > table'
        url2 = url_dict[2] + search2
        python_job1 = PythonJob(url=url1, selector=selector1, name='1')
        python_job2 = PythonJob(url=url2, selector=selector2, name='2')
        python_job1.start()  # 启动线程
        python_job2.start()  # 启动线程

```

