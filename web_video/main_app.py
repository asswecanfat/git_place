from flask import Flask
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
from views import main_blue

app.register_blueprint(main_blue)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
