# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import argparse
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramidAngular import home


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--port', help='specify the port to run on')
    args = parser.parse_args()
    p = 5000
    if args.port:
        p = int(args.port)
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    app = config.make_wsgi_app()
    print 'Running application on port %d' % p
    server = make_server('localhost', p, app)
    server.serve_forever()
