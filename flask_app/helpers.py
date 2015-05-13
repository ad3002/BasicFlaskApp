# -*- coding: utf-8 -*-

import simplejson

def return_error(error):
    return simplejson.dumps({"error": error})
