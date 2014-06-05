# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class SearchHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render('search.html')


    def post(self, *args, **kwargs):
        keyword = self.get_argument('keyword')



        self.write({'result':'nihaonihaonihaonihao'})
