from flask import Config, request
from datetime import timedelta
import logging


class BaseConfig(Config):
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    DEBUG = True
    PROPAGATE_EXCEPTIONS = False  # 设置是否传递异常 , 如果为True, 则flask运行中的错误会显示到网页中, 如果为False, 则会输出到文件中


class RequestFormatter(logging.Formatter):  # 自定义格式化类
    def format(self, record: logging.LogRecord) -> str:
        """每次生成日志时都会调用, 该方法主要用于设置自定义的日志信息
                :param record 日志信息"""
        record.url = request.url
        record.addr = request.remote_addr
        return super().format(record)
