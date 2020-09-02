from . import main
from flask import render_template


@main.app_errorhandler(404)
def error(e):
    print(e)
    return render_template('404.html')


@main.app_errorhandler(406)
def not_start(e):
    print(e)
    return render_template('406.html')
