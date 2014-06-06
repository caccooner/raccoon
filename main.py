# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
import datetime
import os
from raccoon.base_handler import PageHandler
from raccoon.handlers.bind_handler import BindHandler
from raccoon.handlers.bind_handler import BindCallbackHandler
from raccoon.handlers.search_handler import SearchHandler

class RaccoonApplication(tornado.web.Application):

    def __init__(self):

        setting = {
            'debug': True,
            'gzip': False,
            'template_path': os.path.join(os.path.dirname(__file__), 'temp'),
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'static_url_prefix': '/static/',
        }

        handlers = [
            ('/',PageHandler,{'page':'index.html'}),
            ('/portal',PageHandler,{'page':'portal.html'}),
            ('/search',SearchHandler),
            ('/static/*',tornado.web.StaticFileHandler),
            ('/bind/(\w*)',BindHandler),
            ('/bind/callback/(\w*)',BindCallbackHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **setting)


def main():
    print '%s : start server on 8080 port ' % datetime.datetime.now()
    server = tornado.httpserver.HTTPServer(RaccoonApplication())
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()





if __name__ == "__main__":
    main()