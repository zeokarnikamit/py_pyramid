# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import argparse
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import pyramidAngular


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--port', help='specify the port to run on')
    args = parser.parse_args()
    p = 5000
    if args.port:
        p = int(args.port)
    config = Configurator()
    config.add_route('home', '/')
    config.add_route('prob', '/projectEuler')
    config.add_route('page', '/{ipage}')
    config.add_view(pyramidAngular.home, route_name='home')
    config.add_view(pyramidAngular.problems, route_name='prob')
    config.add_view(pyramidAngular.get_page, route_name='page', renderer='json')
    app = config.make_wsgi_app()
    run = 'http://127.0.0.1:%d' % p
    print 'Running application on: %s' % run
    server = make_server('127.0.0.1', p, app)
    server.serve_forever()
