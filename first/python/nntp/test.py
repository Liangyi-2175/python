# from nntplib import NNTP
# # server = NNTP('web.aioe.org')
# server = NNTP('news.ntnu.no')
# print(server.group('comp.lang.python.announce')[0])
# class HTMLDestination:
#     """
#     以html格式显示所有新闻的新闻目的地
#     """
#     def __init__(self, filename=None):
#         if filename:
#             self.filename = filename
#         else:
#             self.filename = 'news.html'
#
#     def receive_items(self):
#         out = open(self.filename, 'w')
#         print("""
#         <html>
#             <head>
#                 <title>Today's News</title>
#             </head>
#             <body>
#             <h1>Today's News</h1>
#         """, file=out)
#
# htmldestinations = HTMLDestination('sss.html')
# htmldestinations.receive_items()
