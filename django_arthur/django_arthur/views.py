import configparser
import datetime
import math
import os

from django.http import HttpResponse
from django.template import loader

#
# VIEWS
#


def index(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


