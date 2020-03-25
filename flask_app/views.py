#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from collections import defaultdict
import simplejson
from flask import render_template, url_for, redirect
from flask import abort, request, flash
from flask_app.models import *
from flask_app import app
from flask_app.settings import *
from flask_app.helpers import return_error
from flask_app.forms import *
from flask_app.workers import *
import time
import datetime
import eventlet
from eventlet.green import urllib2

eventlet.monkey_patch() 

def get_context():

    user = None
    tasks = None

    context = {
        "title": "AppTitle",
    }
    
    return context

@app.route('/')
def index():
    ''' Index page
    '''
    d = get_context() 
    return render_template('index.html', d=d)
