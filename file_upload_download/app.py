from flask import Flask, request, render_template, send_from_directory, flash
from pathlib import Path
import datetime

app = Flask(__name__)
app.config.from_pyfile('config.ini')
file_location = Path('index')


@app.route('/index', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            pos = str(file_location / file.filename)
            file.save(pos)
            p = Path(pos)
            flash(f'文件：{file.filename}(大小：{p.stat().st_size}字节)发送成功！'
                  )
        else:
            flash('未选择文件！')
    return render_template('index.html', data=file_data())


def file_data():
    file_list = list(file_location.glob('*.*'))
    name_list = [i.name for i in file_list]
    big_list = [f'{i.stat().st_size}字节' for i in file_list]
    time_list = [str(datetime.datetime.fromtimestamp(i.stat().st_ctime))
                 for i in file_list]
    return zip(name_list, big_list, time_list)


@app.route('/index/<string:filename>', methods=['get', 'post'])
def file_download(filename):
    return send_from_directory(str(file_location),
                               filename, as_attachment=True)
