from flask import render_template, Flask, request
from pathlib import Path

app = Flask(__name__)


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
    new_file = f'../static/video{file}'
    return render_template('play_video.html', file=new_file)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
