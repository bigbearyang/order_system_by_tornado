import uuid

class Session(object):
    container = {}
    def __init__(self,handler):
        nid = handler.get_cookie('Session_id')
        if nid:
            if nid in Session.container:
                pass
            else:
                nid = str(uuid.uuid4())
                Session.container[nid] = {}
        else:
            nid = str(uuid.uuid4())
            Session.container[nid] = {}

        handler.set_cookie('Session_id', nid, max_age=3000)
        # nid当前访问用户的随即字符串
        self.nid = nid
        # 封装了所有用户请求信息
        self.handler = handler

    def __setitem__(self, key, value):
        Session.container[self.nid][key] =value

    def __getitem__(self, item):
        return Session.container[self.nid].get(item)

    def __delitem__(self, key):
        del Session.container[self.nid][key]

