# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

class BaseHttpHandler(RequestHandler):
    '''
        base http request handler to handler the auth and redirect
    '''

    def get(self, *args, **kwargs):
        self._handle_auth(args, kwargs)

    def post(self, *args, **kwargs):
        self._handle_auth(args, kwargs)

    def _handle_auth(self, *args, **kwargs):
        if not self.current_user :
            self.redirect('/login')
        else:
            self.handler_request(args, kwargs)

    def handler_request(self, *args, **kwargs):
        raise NotImplementedError()




class PageHandler(RequestHandler):
    def initialize(self,page):
        self._page = page
    def get(self, *args, **kwargs):
        self.handle()

    def post(self, *args, **kwargs):
        self.handle()

    def handle(self):
        self.render(self._page)


