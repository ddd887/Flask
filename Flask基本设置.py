import flask
from flask import *

#创建flask程序
app = Flask(__name__)

@app.route('/abc')
def a_page():
    return "this is a page"
    pass

#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run()