from raccoon.util.oath_util import OathConfig
from raccoon.util.oath_util import OauthHandler
from tornado.web import RequestHandler
import logging

LOG = logging.getLogger(__name__)



__OauthHanlderHold = OauthHandler()


class BindHandler(RequestHandler):
    def get(self, bind_type):
        self.redirect(__OauthHanlderHold.get_oauth_handler(bind_type).get_code_redirect_url())



class BindCallbackHandler(RequestHandler):
    def get(self,bind_type):
        code = self.get_argument('code', None)
        if code is None:
            LOG.error(bind_type+': get None code ,retry!')
            self.redirect('/bind/'+bind_type)
        else:
            token_info = __OauthHanlderHold.get_oauth_handler(bind_type).get_token(code)      


