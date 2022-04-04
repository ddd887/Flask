import flask
from flask import *

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templages' #模板文件
            )

@app.route('/b')
def b_page():
    return '来啦'
    pass

@app.route('/redirect')
def a_page():
    #站外
    #return flask.redirect('https://www.baidu.com')
    #站外
    return flask.redirect(flask.url_for('b_page'))
    pass


#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run()