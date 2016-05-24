# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from pyramid.response import Response
from pyramid.response import FileResponse
import os
import requests
import urllib3
from bs4 import BeautifulSoup
import json
from pyramid.view import view_config


def home(request):
    path = os.path.abspath('templates/details.html')
    response = FileResponse(path)
    return response


def problems(request):
    path = os.path.abspath('templates/proj_euler.html')
    resp = FileResponse(path)
    return resp


@view_config(renderer='json')
def get_page(request):
    data = {"response": "failure"}
    try:
        http = urllib3.PoolManager()
        page = request.matchdict['ipage']
        url = 'https://projecteuler.net/problem=' + str(page)
        resp = http.request('GET', url)
        if resp.status == 200:
            soup = BeautifulSoup(resp.data, 'html.parser')
            result_set = soup.find(role='problem').find_all('p')
            res_list = []
            for i in result_set:
                res_list.append(i.text)
            data['data'] = res_list
            data['response'] = 'success'
    except Exception, e:
        data['Error'] = e
    return data


def hello_world(request):
    name = request.matchdict['iname']
    age = int(request.matchdict['age'])
    return Response('Hello %dyrs old %s' % (age, name))
