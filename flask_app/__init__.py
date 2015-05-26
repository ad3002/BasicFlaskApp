#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from flask import Flask
from settings import *
from flask.ext.basicauth import BasicAuth

app = Flask('flask_app')
app.config.from_object('flask_app.settings')
app.config['DEBUG'] = DEBUG

app.secret_key = 'asfu32ff3afap'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['BASIC_AUTH_USERNAME'] = BASIC_AUTH_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = BASIC_AUTH_PASSWORD
app.config['BASIC_AUTH_FORCE'] = BASIC_AUTH_FORCE

basic_auth = BasicAuth(app)

import views
import filters