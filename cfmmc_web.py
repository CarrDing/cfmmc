import json
from abc import ABC

import tornado.ioloop
import tornado.web
import cfmmc as cf


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        """get请求"""
        account = self.get_argument('account')
        passwd = self.get_argument('passwd')
        print(passwd)
        print(account)
        # cf.do(account, passwd)
        self.write(str(cf.do(account, passwd)))


application = tornado.web.Application([(r"/cfmmc", MainHandler), ])

if __name__ == "__main__":
    application.listen(8868)
    tornado.ioloop.IOLoop.instance().start()

