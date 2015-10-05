# -*- coding: utf-8 -*-

import sys   
#sys.path.append("..")  

from bottle import *
from bottle import __version__ as bottleVer
from bottle import jinja2_template as template
from config import JINJA2TPL_PATH
TEMPLATE_PATH.insert(0, JINJA2TPL_PATH)

from config import CFG
#debug(True)
APP = Bottle()

#APP.mount('/up', __import__('mana4up').APP)
APP.mount('/api', __import__('mana4api').APP)
APP.mount('/wx1', __import__('api4devr').APP)
#APP.mount('/mana', __import__('mana4sys').APP)


#@view('404.html')
@APP.get('/')
def index():
    #return template('index.html')
    return """%s 
    esp. support wechat public No.: PyChina
    ; only API service !-)
    contact: sipport@devrel.info
    """% CFG.VERSION

#@view('404.html')
@APP.error(404)
def error404(error):
    return '''


\          SORRY            /
 \                         /
  \    This page does     /
   ]   not exist yet.    [    ,'|
   ]                     [   /  |
   ]___               ___[ ,'   |
   ]  ]\             /[  [ |:   |
   ]  ] \           / [  [ |:   |
   ]  ]  ]         [  [  [ |:   |
   ]  ]  ]__     __[  [  [ |:   |
   ]  ]  ] ]\ _ /[ [  [  [ |:   |
   ]  ]  ] ] (#) [ [  [  [ :===='
   ]  ]  ]_].nHn.[_[  [  [
   ]  ]  ]  HHHHH. [  [  [
   ]  ] /   `HH("N  \ [  [
   ]__]/     HHH  "  \[__[
   ]         NNN         [
   ]         N/"         [
   ]         N H         [
  /          N            \

/                           \

roaring zoomquiet+404@gmail.com
'''
#    return template('404.html')

@APP.route('/favicon.ico')
def favicon():
    abort(204)
    
@APP.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')
    

if __name__ == '__main__':
    debug(True)
    #0.0.0.0
    run(app, host="0.0.0.0",reloader=True)
