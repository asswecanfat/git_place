from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from stu_project.app import creat_app
from tornado.ioloop import IOLoop


if __name__ == '__main__':
    app = creat_app('default')
    s = HTTPServer(WSGIContainer(app))
    s.listen(9900)  # 监听 9900 端口
    IOLoop.current().start()
