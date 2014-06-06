import urllib
import urllib2
import json


class OauthHandler():
    def __init__(self):
        self.cache = {}
        for key,val in OathConfig.iteritems():
            self.cache.setdefault(key,OathConfig.get(key).get('util')())  
            
    def get_oauth_handler(self, key):
        return self.cache.get(key)

       

class LinkedinUtil(object):
    _type = 'linkedin'
    _field_select = ':(id,first-name,last-name,formatted-phonetic-name,headline,email-address,skills,educations,industry,summary,positions,three-current-positions,picture-url,public-profile-url,api-standard-profile-request,site-standard-profile-request)'
    def get_code_redirect_url(self):
        api_config = OathConfig.get(self._type)
        params = {'response_type':'code', 'client_id':api_config.get('client_id'), 'scope': api_config.get('scope'), 'state':api_config.get('state'), 'redirect_uri': api_config.get('redirect_url')}
        return api_config.get('auth_code_url') +'?'+urllib.urlencode(params)
    
    def get_token(self,handler,code):
        api_config = OathConfig.get(self._type)
        params = {'grant_type':'authorization_code','code':code,'redirect_uri':api_config.get('redirect_url'),'client_id':api_config.get('client_id'),'client_secret':api_config.get('client_secret')}
        url = api_config.get('auth_token_url')+'?'+urllib.urlencode(params)
        resp = urllib2.urlopen(url)
        token_json = json.load(resp.read()) 
        token = token_json['access_token']
        expires_in = token_json['expires_in']
#         store in 

    def get_base_profile(self,token):
        url = 'http://api.linkedin.com/v1/people/~'+self._field_select+'?oauth2_access_token='+token
        resp = urllib2.urlopen(url)
        return resp.read()
   
    def search_people(self,token,keywords,**kwargs):
        kwargs['oauth2_access_token'] = token
        url = 'http://api.linkedin.com/v1/people-search:(people'+self._field_select+',100)?keywords='+keywords+'&'+urllib.urlencode(kwargs)
        resp = urllib2.urlopen(url)
        return resp.read()
    
    def get_connections(self,token):
        url = 'http://api.linkedin.com/v1/people/~/connections'+self._field_select+'?oauth2_access_token='+token
        resp = urllib2.urlopen(url)
        return resp.read()

class SinaWeiboUtil():
    _type = 'SinaWeibo'
    def get_code_redirect_url(self):
        pass
    def get_token(self,handler,code):
        pass
    def get_base_profile(self,token):
        pass
    def search_people(self,token,keywords,**kwargs):
        pass
    def get_connections(self,token):
        pass
    
class LiepingUtil():
    _type = 'SinaWeibo'
    _auth = 'direct'
    def get_code_redirect_url(self):
        pass
    def get_token(self,handler,code):
        pass
    def get_base_profile(self,token):
        pass
    def search_people(self,token,keywords,**kwargs):
        pass
    def get_connections(self,token):
        pass
    
    
    
OathConfig={
    'linkedin':{
        'util':LinkedinUtil,
        'client_id':'75d6qv93etmv1u',
        'client_secret':'QbNYhFLTikbD0k3x',
        'redirect_url':'http://www.mi.com/',
        'auth_code_url':'https://www.linkedin.com/uas/oauth2/authorization',
        'auth_token_url':'https://www.linkedin.com/uas/oauth2/accessToken',
        'scope':'r_fullprofile r_contactinfo r_emailaddress',
        'state':'DCEEFWF45453sdffef424',
    },

}

