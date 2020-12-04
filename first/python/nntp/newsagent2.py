import ssl
from nntplib import NNTP, decode_header
import urllib.request
import textwrap
import re
ssl._create_default_https_context = ssl._create_unverified_context
from abc import abstractmethod, ABC


class NewsAgent:
    """
    可将新闻源中的新闻分发到新闻目的地的对象
    """

    def __init__(self):
        self.sources = []
        self.destinations = []  # type:

    def add_source(self, source):
        self.sources.append(source)

    def addDestinations(self, dest: 'AbstractClass'):
        self.destinations.append(dest)

    def distribute(self):
        """
        从所有的新闻源获取所有的新闻，并将其分发到所有的新闻目的地
        :return:
        """
        items = []
        for source in self.sources:
            print(111)
            # extend(1) 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
            items.extend(source.get_items())
        for dest in self.destinations:
            dest.receive_items(items)


class AbstractClass(ABC):

    @abstractmethod
    def receive_items(self, items):
        pass


class NewItem:
    """
    由标题和正文组成的简单新闻
    """

    def __init__(self, title, body):
        self.title = title
        self.body = body


class NNTPSource:
    """
    从NNTP新闻组获取新闻的新闻源
    """

    def __init__(self, servername, group, howmany):
        self.servername = servername
        self.group = group
        self.howmany = howmany

    def get_items(self):
        print(222)
        server = NNTP(self.servername)
        resp, count, first, last, name = server.group(self.group)
        start = last - self.howmany + 1
        resp, overviews = server.over((start, last))
        for id, over in overviews:
            title = decode_header(over['subject'])
            resp, info = server.body(id)
            body = '\n'.join(line.decode('latin') for line in info.lines) + '\n\n'
            yield NewItem(title, body)

        server.quit()


class SimpleWebSource:
    """
    使用正则表达式从网页提取新闻的新闻源
    """

    def __init__(self, url, title_pattern, body_pattern, encoding='utf-8'):
        self.url = url
        self.title_pattern = title_pattern
        self.body_pattern = body_pattern
        self.encoding = encoding

    def get_items(self):
        print(333)
        print(f'url:{self.url}')
        text = urllib.request.urlopen(self.url).read().decode(self.encoding)
        print(f'text:{text}')
        titles = re.findall(self.title_pattern, text)
        bodies = re.findall(self.body_pattern, text)
        for title, body in zip(titles, bodies):
            yield NewItem(title, textwrap.fill(body) + '\n')


class PlainDestination(AbstractClass):
    """
    以纯文本方式显示所有新闻的新闻目的地
    """

    def receive_items(self, items):
        for item in items:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)


class HTMLDestination(AbstractClass):
    """
    以html格式显示所有新闻的新闻目的地
    """

    def __init__(self, filename):
        self.filename = filename

    def receive_items(self, items):
        out = open(self.filename, 'w')
        print("""
        <html>
            <head>
                <title>Today's News</title>
            </head>
            <body>
            <h1>Today's News</h1>
        """, file=out)

        print('<ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print(f' <li><a href="#{id}">{item.title}</a></li>', file=out)
        print('</ul>', file=out)

        id = 0
        for item in items:
            id += 1
            print(f'<h2><a name="{id}">{item.title}</a></h2>', file=out)

        print("""
        </body>
            </html>
        """, file=out)


def runDefaultSetup():
    """
    默认的新闻源和目的地设置，请根据偏好进行修改
    :return:
    """
    agent = NewsAgent()
    # 从路透社获取新闻的SimpleWebSource对象：
    reuters_url = 'http://www.reuters.com/news/world'
    reuters_url = 'http://www.hupu.com/'
    reuters_title = r'<h2><a href="[^"]*"\s*>(.*?)</a>'
    reuters_body = r'</h2><p>(.*?)</p>'
    reuters = SimpleWebSource(reuters_url, reuters_title, reuters_body)
    agent.add_source(reuters)
    # 从comp.lang.python.announce获取新闻的NNTPSource对象：
    clpa_server = 'news.foo.bar'  # 替换为实际服务器的名称
    clpa_server = 'news.ntnu.no'
    clpa_server = 'web.aioe.org'
    clpa_group = 'comp.lang.python.announce'
    clpa_howmany = 1
    clpa = NNTPSource(clpa_server, clpa_group, clpa_howmany)
    agent.add_source(clpa)
    # 添加纯文本目的地和HTML的目的地：
    agent.addDestinations(PlainDestination())
    agent.addDestinations(HTMLDestination("news.html"))

    # 分发新闻：
    agent.distribute()


if __name__ == '__main__':
    runDefaultSetup()
