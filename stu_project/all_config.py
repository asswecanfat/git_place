from datetime import timedelta
from flask_uploads import IMAGES
from pathlib import Path

img_path = Path('./app/static/data')
ip = '127.0.0.1:5000'


class BaseConfig:
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    PROPAGATE_EXCEPTIONS = False
    # 设置是否传递异常 , 如果为True, 则flask运行中的错误会显示到网页中, 如果为False, 则会输出到文件中
    DEBUG = True
    SECRET_KEY = '123'
    WTF_CSRF_ENABLED = False  # 关闭CSRF检验
    UPLOADED_PHOTOS_DEST = './app/static/data'  # 配置文件保存的目录，本参数必须设置；
    UPLOADED_PHOTOS_ALLOW = IMAGES  # 配置允许的扩展名，其他的都是不允许
    UPLOADED_PHOTOS_DENY = ['html', 'php']  # 配置不允许的扩展名
    SQLALCHEMY_DATABASE_URI = 'mysql://root:99271727@127.0.0.1:3306/sign_in?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


config = {'base_config': BaseConfig, 'default': BaseConfig}
