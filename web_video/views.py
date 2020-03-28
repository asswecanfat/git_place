from flask import Blueprint, render_template
from pathlib import Path
from logging.handlers import RotatingFileHandler
from config import RequestFormatter
import json

main_blue = Blueprint('main', __name__)
video_file = ['.flv', '.mp4', '.mkv']

from main_app import app


@main_blue.app_errorhandler(404)
def error(e):
    app.logger.error(f'访问页面出错:{e}')
    return render_template('404.html')


@main_blue.before_app_first_request
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


@main_blue.route('/asswecan', methods=['get', 'post'])   # 主页
def asswecan():
    return render_template('asswecan.html')


def get_vedio_list(vedio_floder: Path, vedio_floder_name: str):
    vedio_list = []
    for i in vedio_floder.glob('*'):
        if i.suffix in video_file:
            vedio_list.append(f'../static/video/{vedio_floder_name}/{str(i.name)}')
    return vedio_list


@main_blue.route('/vedio_api', methods=['get', 'post'])
def return_json():
    this_dir = Path(__file__).absolute().parent / Path(r'static/video')
    vedio_json = json.dumps([{'imgSrc': f'static/video/{i.name}/1.jpg',
                              'name': i.name,
                              'src': get_vedio_list(Path(i), i.name),
                              'index': num + 1} for num, i in enumerate(this_dir.glob('*'))])
    return vedio_json
