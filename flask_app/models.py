#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 16.04.2015
#@author: Alex Ferechin
#@contact: alex.ferechin@gmail.com 

import pymongo
from pymongo import MongoClient as Connection
from PyExp import AbstractModel
from flask_app.settings import *
import os
import subprocess
from flask_app import app
from flask import redirect, flash

TABLE_NAME = "SomeTable"

db_table = Connection("localhost", 27017)[APP_NAME][TABLE_NAME]

def create_settings_obj():
	obj = db_settings.find_one({"_id": "global"})
	if not obj:
		obj = {"_id": "global"}
		db_settings.save(obj)
	return obj

@app.route('/upload/data')
def upload_all():
    """
    """
    ps = []
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    upload_commands = [
        "mongoimport -d %s -c %s -f rank,_id --type csv --upsert --file %s" % (APP_NAME, TABLE_NAME, os.path.join(current_dir, "static/alexa.csv")),
        
    ]
    for upload_command in upload_commands:
        ps.append(subprocess.check_output(upload_command, stderr=subprocess.STDOUT, shell=True))
    for p in ps:
        flash('A process returned: %s' % p)
    return redirect("/")