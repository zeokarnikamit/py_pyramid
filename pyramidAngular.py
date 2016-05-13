# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from pyramid.response import Response
from pyramid.response import FileResponse
import os


def home(request):
    path = os.path.abspath('templates/details.html')
    response = FileResponse(path)
    return response


def hello_world(request):
    name = request.matchdict['iname']
    age = int(request.matchdict['age'])
    return Response('Hello %dyrs old %s' % (age, name))

