# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from pyramid.response import Response


def hello_world(request):
    name = request.matchdict['iname']
    age = int(request.matchdict['age'])
    return Response('Hello %dyrs old %s' % (age, name))
