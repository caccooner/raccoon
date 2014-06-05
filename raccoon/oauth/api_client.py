__author__ = 'carvee'

class ApiClient():
    def __init__(self,user,pwd):
        self._user = user
        self._pwd  = pwd

    def get_token(self):
        raise NotImplementedError()

    def get_profile(self):
        raise NotImplementedError()

    def get_connections(self):
        raise NotImplementedError()

    def search_candidate(self,**kwargs):
        raise NotImplementedError()

    def share_position_info(self,title,content,**kwargs):
        raise NotImplementedError()