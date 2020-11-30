from urllib import request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Spider:
    url = 'https://www.douyu.com/directory/all'
    root_parrern = '<div class="DyListCover-info">[\s\S]*?</div>'
    name_parrern = '<i class="DyListCover-info">[\s\S]*?</i>'

    def _fetch_context(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def _analysis(self, htmls):
        root_html = re.findall(Spider.root_parrern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_parrern, html)
            number = re.findall(Spider.number_patern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)

    def go(self):
        htmla = self._fetch_context()
        self._analysis(htmla)



spider = Spider()
spider.go()
