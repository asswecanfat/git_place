import random
import base64


class Config:
    SECRET_KEY = base64.b64encode(bytes(random.randint(100000, 19999999)))
    DEBUG = True  # 关闭debug