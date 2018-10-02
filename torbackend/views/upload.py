from tornado.web import RequestHandler
import json
from models.image import Image
import re
from common.libs.uploadservice import UploadService
from common.libs.urlmanager import UrlManager
from models import session
from config import BASE_DIR

class UeditorHandler(RequestHandler):
    def get(self, *args, **kwargs):
        action = self.get_argument('action', '')
        if action == "config":
            config_path = "{0}/static/plugins/ueditor/upload_config.json".format(BASE_DIR)
            with open(config_path, encoding="utf-8") as fp:
                try:
                    config_data = json.loads(re.sub(r'\/\*.*\*/', '', fp.read()))
                except:
                    config_data = {}
            self.finish(config_data)
            return

        if action == "listimage":
            self.finish(listImage(self))
            return

        self.finish('upload')

    def post(self, *args, **kwargs):
        action = self.get_argument('action', '')
        if action == "uploadimage":
            self.finish(uploadImage(self))

def uploadImage(self):
    resp = {'state': 'SUCCESS', 'url': '', 'title': '', 'original': ''}
    # file_target 是一个字典
    file_target = self.request.files
    upfile = file_target['upfile']
    if upfile is None or len(upfile) == 0:
        resp['state'] = "上传失败"
        self.finish(resp)
        return

    ret = UploadService.uploadByFile(upfile[0])
    if ret['code'] != 200:
        resp['state'] = "上传失败：" + ret['msg']
        self.finish(resp)
        return

    resp['url'] = UrlManager.buildImageUrl(ret['data']['file_key'])
    return resp


def listImage(self):
    resp = {'state': 'SUCCESS', 'list': [], 'start': 0, 'total': 0}
    start = int(self.get_argument('start',0))
    page_size = int(self.get_argument('size',20))

    query = session.query(Image)
    if start > 0:
        query = query.filter(Image.id < start)

    list = query.order_by(Image.id.desc()).limit(page_size).all()
    images = []

    if list:
        for item in list:
            images.append({'url': UrlManager.buildImageUrl(item.file_key)})
            start = item.id
    resp['list'] = images
    resp['start'] = start
    resp['total'] = len(images)
    return resp


class UploadPicHandler(RequestHandler):
    def post(self, *args, **kwargs):
        file_target = self.request.files
        upfile = file_target['pic']
        callback_target = 'window.parent.upload'
        if upfile is None or len(upfile) == 0:
            self.write("<script type='text/javascript'>{0}.error('{1}')</script>".format(callback_target, "上传失败"))
            return
        ret = UploadService.uploadByFile(upfile[0])
        if ret['code'] != 200:
            self.write("<script type='text/javascript'>{0}.error('{1}')</script>".format(callback_target,
                                                                                     "上传失败：" + ret['msg']))
            return

        self.finish("<script type='text/javascript'>{0}.success('{1}')</script>".format(callback_target,
                                                                                   ret['data']['file_key']))

