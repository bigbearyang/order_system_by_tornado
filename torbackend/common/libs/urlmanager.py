from config import UPLOAD,Server

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildImageUrl(path):
        url = Server['domain'] + UPLOAD['prefix_url'] + path
        return url