#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import os
import argparse

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from flask_app import app

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run application')
    parser.add_argument('-p','--port', help='Port', default=3015)
    args = vars(parser.parse_args())
    port = int(args["port"])
    app.run(host='0.0.0.0', port=port)
