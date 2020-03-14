from . import main
from flask import render_template


@main.app_errorhandler(404)
def error(e):
    print(e)
    return render_template('error.html')
