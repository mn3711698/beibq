#coding:utf-8

import os
import sys
from imp import reload
reload(sys)

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

from app import create_app
#from flask_script import Manager

app = create_app()

#manager = Manager(app)

if __name__ == "__main__":
    app.run()

application=app