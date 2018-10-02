import tornado.ioloop
from application import Application
from tornado.options import define, options
define("port", default=8000, help="run on the given port ", type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

