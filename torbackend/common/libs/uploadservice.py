import datetime
import os
import stat
import uuid

from werkzeug.utils import secure_filename

from common.libs.helper import getCurrentDate
from config import UPLOAD,BASE_DIR
from models import session
from models.image import Image


class UploadService():
    @staticmethod
    def uploadByFile(file):
        resp = {'code':200,'msg':'操作成功~~','data':{}}
        filename = secure_filename(file.get('filename'))
        ext = filename.rsplit(".",1)[1]
        if ext not in UPLOAD['ext']:
            resp['code'] = -1
            resp['msg'] = "不允许的扩展类型文件"
            return resp

        root_path = BASE_DIR + UPLOAD['prefix_path']
        file_dir = datetime.datetime.now().strftime("%Y%m%d")
        save_dir = root_path + file_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            os.chmod(save_dir,stat.S_IRWXU | stat.S_IRGRP |  stat.S_IRWXO)

        file_name = str(uuid.uuid4()).replace("-","") + "." + ext

        with open(save_dir+'/'+ file_name,'wb') as f:
            f.write(file["body"])

        model_image = Image()
        model_image.file_key = file_dir + "/" + file_name
        model_image.created_time = getCurrentDate()
        session.add(model_image)
        session.commit()

        resp['data'] = {
            'file_key': model_image.file_key
        }
        return resp