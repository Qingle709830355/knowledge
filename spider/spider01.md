# 使用urllib爬取搜狐新闻并存储进mysql

```Python
import re
from urllib import request
import pymysql


def resvole_html(url):
    """
    解析主页面
    :param url: 主页面的url
    :return: 返回主页面的源码
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    req = request.Request(url=url, headers=headers)  # 请求页面， 返回一个response对象
    res = request.urlopen(req)  # 打开response对象
    return res.read()


def decode_html(html, charsets=('gbk', 'utf-8')):
    """
    解码主页面
    :param html: 主页面的源码
    :param charsets: 主页面charset的格式
    :return: 解码后的或解码出错的
    """
    page_html = ''
    for charset in charsets:
        try:
            page_html = html.decode(charset)
            break
        except:
            pass
    return page_html


def base_regx(page_html, regx):
    """
    基础的正则匹配
    :param page_html: 页面的源码，
    :param regx: 正则表达式
    :return: 返回我们想要的通过正则表达市匹配的数据
    """
    regx_html = re.compile(regx, re.S)
    return regx_html.findall(page_html) if page_html else []


def get_list(url, url_re):
    """
    获取正则匹配的所有元素的列表
    :param url:  需要请求的页面
    :param url_re:  想要匹配的数据的正则表达式
    :return:  返回匹配后的数据列表
    """
    html = resvole_html(url)  # 获取页面源码
    page_html = decode_html(html)  # 解码页面源码
    # <a test="a" href="https://www.sohu.com/a/237805527_458722" target="_blank">西蒙斯：感谢家人和好友 队友教练以及整个费城</a>
    after_html = base_regx(page_html, url_re)  # 正则匹配
    return after_html


def conn_mysql(sql, sql_list):
    """
    连接数据库并插入数据
    :param sql:  插入数据库  insert...
    :param sql_list:  所有需要插入的数据列表
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           password='123456', charset='utf8', db='spider')
    cursor = conn.cursor()
    cursor.executemany(sql, sql_list)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    url = 'http://sports.sohu.com/nba_a.shtml'  # 需要请求的页面
    url_re = "<a test=a href='(.*?)' target=.*?"  # 想要匹配的内容的正则表达式
    url_list = get_list(url, url_re)  # 获取所有url的列表
    title_re = '<h1>(.*?)<span.*?'  # 正则匹配标题
    content_re = '<article class="article" id="mp-editor">(.*?)</article>'  # 正则匹配内容
    sql_list = []
    sql = 'insert into souhu_sports (title, content) VALUES  (%s, %s)'  # 插入语句
    for one_url in url_list:
        title = get_list(one_url, title_re)  # 获取title
        content = get_list(one_url, content_re)  # 获取内容
        sql_list.append([title, content])  # 将数据添加进列表
    conn_mysql(sql, sql_list)  # 连接数据库，并批量插入数据
    print('OK')
```

