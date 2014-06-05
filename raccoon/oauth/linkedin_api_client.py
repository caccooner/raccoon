import json
import urllib
import mechanize
from tornado import httpclient,curl_httpclient
from raccoon.oauth.api_client import ApiClient
from tornado import gen
__author__ = 'carvee'

LinkedInConfig = {
    'api_url' :{
        'people':'https://api.linkedin.com/v1/people/%s',
        'connection':'https://api.linkedin.com/v1/people/%s/connections',
    },

    'debug' : True,
    ########### app info #######################
    'HOST' : 'https://www.linkedin.com',
    'OAUTH_GET_CODE' : '/uas/oauth2/authorization',
    'OAUTH_GET_TOKEN' : '/uas/oauth2/accessToken',
    'client_id' : '75d6qv93etmv1u',
    'scope' : 'r_fullprofile r_emailaddress r_network r_contactinfo rw_nus rw_company_admin rw_groups w_messages',
    'redirect_uri' : 'http://www.mi.com/',
    'client_secret' : 'QbNYhFLTikbD0k3x',
}


class LinkedInApiClient(ApiClient):

    def __init__(self, user, pwd):
        super(ApiClient, self).__init__(user, pwd)

        self._client = httpclient.AsyncHTTPClient()
        self._token = self.get_token()

    @gen.coroutine
    def get_token(self):
        params = {'response_type': 'code','client_id': LinkedInConfig.client_id,'scope':LinkedInConfig.scope ,'redirect_uri':LinkedInConfig.redirect_uri ,'state':'DCEEFWF45453sdffef424'}

        headers = httpclient.httputil.HTTPHeaders()
        headers.add('User-agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')

        request = httpclient.HTTPRequest(LinkedInConfig['HOST']+LinkedInConfig['OAUTH_GET_CODE'], headers)

        response = yield self._client.fetch(request)
        self._add_cookie(response,headers)

        return response.body


    def _add_cookie(self,response,headers):
        for cookie in response.headers.get_list('Set-Cookie'):
            headers.add('Cookie',cookie)



