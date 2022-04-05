import flask
from flask import *

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templates' #模板文件
            )

@app.route('/b')
def b_page():
    response = flask.make_response('success')
    #设置cookie
    response.set_cookie('user_id','10',max_age=50)
    response.set_cookie('vip','0',max_age=50)
    return response
    pass

@app.route('/a')
def a_page():
    #读取cookie
    user_id = request.cookies.get('user_id')
    vip = request.cookies.get('vip')
    return flask.render_template("tempa.html",user_id=user_id,vip=vip)
    pass


@app.route('/logout')
def logout():
    response = flask.make_response('退出')
    response.delete_cookie('user_id')
    response.delete_cookie('vip')
    return response

#装饰器,关联路由
@app.route('/')
def index():
    return "haha"
    pass

#404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404
    pass

if __name__ == '__main__':
    app.run()
