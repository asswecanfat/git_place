from . import main
from .form import PostForm
from .. import db, photos
from ..models import Stu, Sign
from ... import all_config

from flask import render_template, abort, request
from datetime import datetime, timedelta
from pathlib import Path
from .file_deal import deal_hash, get_time


user_dict = None
end_time = datetime.now()
flag = 0


@main.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    global user_dict
    global end_time
    global flag
    form = PostForm()
    message = ''
    if not flag:
        abort(404)
    if datetime.now() > end_time:
        flag = 0
        abort(404)
    if form.validate_on_submit() and 'photo' in request.files:
        form_data = request.form
        user_name = form_data['username']
        user_id = form_data['student_id']
        if user_dict.get(user_id) == user_name:
            img_file = request.files['photo']
            file_type = Path(img_file.filename).suffix
            img_name = '{}{}'.format(deal_hash(str(Path(f'{user_id}{user_name}')) + str(datetime.today())),
                                     file_type)
            try:
                data = Sign(user_id, user_name, str(datetime.today()), f'http://{all_config.ip}/pic_show/{img_name}')
                db.session.add(data)
                db.session.commit()
                photos.save(storage=img_file, name=str(img_name))
            except BaseException as e:
                print(e)
                db.session.rollback()
                message = '签到失败，数据记录错误！'

            else:
                message = '签到成功！'
        else:
            message = '签到失败，学号与姓名不匹配！'
    return render_template('index.html', form=form, message=message, time=get_time(end_time))


@main.route('/pic_show/<string:img_name>', methods=['POST', 'GET'])
def show(img_name):
    return render_template('show.html', img_url=f'../static/data/{img_name}')


@main.before_app_first_request
def creat():
    global user_dict
    user_list = Stu.query.all()
    user_dict = {str(i.id): i.name for i in user_list}


@main.route('/start', methods=['POST', 'GET'])
def start():
    global end_time
    global flag
    flag = 1
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=20)
    return '200'
