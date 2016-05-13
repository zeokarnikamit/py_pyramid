# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import argparse
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from helloworld import hello_world



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--port', help='specify the port to run on')
    args = parser.parse_args()
    p = 5000
    if args.port:
        p = int(args.port)
    config = Configurator()
    config.add_route('hi', '/hi/{iname}/{age}')
    config.add_view(hello_world, route_name='hi')
    app = config.make_wsgi_app()
    print 'Running application on port %d' % p
    server = make_server('0.0.0.0', p, app)
    server.serve_forever()
