from flask import render_template, Flask, request
from pathlib import Path
from config import BaseConfig, RequestFormatter
from logging.handlers import RotatingFileHandler
import logging


app = Flask(__name__)
app.config.from_object(BaseConfig)


@app.route('/videolist', methods=['POST', 'GET'])
def get_list():
    file_dict = get_dir()
    return render_template('video_list.html', file_dict=file_dict)


def get_dir():
    target = 'static/video'
    p = Path(target)
    return {i.name: [j.name for j in Path(i).iterdir()] for i in p.iterdir()}


@app.route('/play', methods=['get', 'post'])
def play():
    file = request.args.get('file')
    deal = Path(file)
    new_file = f'../static/video{file}'
    return render_template('play_video.html', file=new_file, file_name=deal.stem)


@app.errorhandler(404)
def error(e):
    print(e)
    app.logger.error('访问页面出错')
    return render_template('404.html')


@app.before_first_request
def creat_log():
    # 设置全局级别
    app.logger.setLevel('DEBUG')
    # 创建文件处理器
    file_handler = RotatingFileHandler(filename='./static/server.log', maxBytes=100 * 1024 * 1024,
                                       backupCount=10)
    # 给处理器设置输出格式
    file_formatter = RequestFormatter(fmt='[%(asctime)s]-%(addr)s-访问-%(url)s-%(name)s-%(levelname)s-%('
                                          'lineno)d-%(message)s')
    file_handler.setFormatter(file_formatter)
    # 单独设置文件处理器的日志级别
    file_handler.setLevel('NOTSET')
    # 日志器添加处理器
    app.logger.addHandler(file_handler)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
