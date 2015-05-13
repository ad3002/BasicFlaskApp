#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 16.04.2015
#@author: Alex Ferechin
#@contact: alex.ferechin@gmail.com 

"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flask.ext import wtf
from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import Required 
from models import db_users
import hashlib

class LoginForm(wtf.Form):
    email = TextField('Email', [Required()])
    password = PasswordField('Password', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = db_users.find_one({"email":self.email.data})
        
        if user is None:
            self.email.errors.append('Unknown email')
            return False

        pw_hash = hashlib.sha224(self.password.data).hexdigest()
        if not user.password == pw_hash:
            self.password.errors.append('Invalid password')
            return False
            
        self.user = user
        return True
